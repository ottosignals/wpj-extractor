import os
import datetime

from bigquery.api import BigQueryApi
from wpj.api import WPJApi
from wpj.queries.orders import bq_schema as orders_bq_schema

def run():
  PROJECT_ID = os.environ.get('PROJECT_ID')
  DATASET_ID = os.environ.get('DATASET_ID')
  TABLE_ID = os.environ.get('TABLE_ID')

  API_KEY = os.getenv("API_KEY")
  API_DOMAIN = os.getenv("API_DOMAIN")
  API_METHOD = os.getenv("API_METHOD", 'orders')
  
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
    bq.insert(PROJECT_ID, DATASET_ID, TABLE_ID, rows, schema=orders_bq_schema)


run()




