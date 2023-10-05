import requests
import pandas as pd
import os
from bigquery.api import BigQueryApi
import models.orders
import datetime
from decorators.retry import retry


class WPJApiError(Exception):
    pass

class WPJApi():
  def __init__(self, domain, api_key):
    self._domain = domain
    self._url_base = f'https://{domain}/admin/graphql/'
    self._headers = {
      "X-Access-Token": f"{api_key}"
    }
  
  @retry(tries=3, delay=10, max_delay=60, backoff=2)
  def send_request(self, body):
    response = requests.get(url=self._url_base, json={"query": body}, headers=self._headers)
    print("response status code: ", response.status_code)
    if response.status_code != 200:
      raise WPJApiError(f"WPJ Api Error with status code: {response.status_code}")
    return response

  def get_orders(self, params):
    body = models.orders.query.format(**params)
    response = self.send_request(body)
    orders_json = response.json().get("data",{}).get("orders",{})
    return orders_json
  
  def get_orders_pagination(self, limit=100, filter=None):
    params = {"offset": 0, 'limit': limit, 'sort': '{dateCreated: ASC}', 'filter': '{}'}
    if filter:
      params["filter"] = """{{
        dateFrom: "{dateFrom}",
        dateTo: "{dateTo}"
      }}""".format(**filter)

    data = []
    while True:
      response = self.get_orders(params)
      print(response)
      items = response.get('items', [])
      data.extend(items)
      print(f'Offset: {params["offset"]}, size: {len(items)}, hasNextPage: {response.get("hasNextPage", False)}')

      if response.get("hasNextPage", False) != True:
        break

      params["offset"] += len(items)
    return data


def run():
  PROJECT_ID = os.environ.get('PROJECT_ID')
  DATASET_ID = os.environ.get('DATASET_ID')
  TABLE_ID = os.environ.get('TABLE_ID')

  API_KEY = os.getenv("API_KEY")
  API_DOMAIN = os.getenv("API_DOMAIN")
  API_METHOD = os.getenv("API_METHOD")
  
  params = {
    "dateFrom": os.environ.get('date_from'),
    "dateTo": os.environ.get('date_to'),
    "numOfDays": int(os.environ.get('num_of_days', 1))
  }

  if params["dateFrom"]:
    params["dateFrom"] = datetime.datetime.strptime(params["dateFrom"], '%Y-%m-%d').isoformat(sep=' ')
    params["dateTo"] = datetime.datetime.strptime(params["dateTo"], '%Y-%m-%d').isoformat(sep=' ')
  else:
    params["dateFrom"] = datetime.datetime.now() - datetime.timedelta(days=params["numOfDays"])
    params["dateFrom"] = params["dateFrom"].replace(hour=0, minute=0, second=0, microsecond=0).isoformat(sep=' ')
    params["dateTo"] = datetime.datetime.now() 
    params["dateTo"] = params["dateTo"].replace(hour=0, minute=0, second=0, microsecond=0).isoformat(sep=' ')

  api = WPJApi(API_DOMAIN, API_KEY)
  bq = BigQueryApi()
  if API_METHOD == 'orders':
    rows = api.get_orders_pagination(limit=100, filter=params)
    bq.insert(PROJECT_ID, DATASET_ID, TABLE_ID, rows, schema=models.orders.schema)


run()




