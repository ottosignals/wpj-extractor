import requests
from .decorators.retry import retry
from .queries import orders

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
    body = orders.gql_query.format(**params)
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