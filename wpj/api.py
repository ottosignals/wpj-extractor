import requests
from .decorators.retry import retry
from .queries import orders, products, sales, users

class WPJApiError(Exception):
    pass

def convert_to_graphql_object(d):
    if isinstance(d, str):
       return d
    items = []
    for key, value in d.items():
        if isinstance(value, dict):
            # If the value is a nested dictionary, recursively convert it
            nested_object = convert_to_graphql_object(value)
            items.append(f'{key}: {nested_object}')
        else:
            items.append(f'{key}: "{value}"')
    return "{" + ", ".join(items) + "}"

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

  def get_query(self):
    body = self._query.format(**self._params)
    response = self.send_request(body)
    data_json = response.json().get("data", {}).get(self._method, {})
    return data_json
  
  def get_query_pagination_init(self, method, limit, sort={}, filter={}):
    self.pagination_end = False
    self._params = {"offset": 0, 'limit': limit, 'sort': convert_to_graphql_object(sort), 'filter': convert_to_graphql_object(filter)}
    self._method = method
    self._query = gql_query = {
        "orders": orders.gql_query,
        "products": products.gql_query,
        "sales": sales.gql_query,
        "users": users.gql_query
    }.get(method)
    if gql_query is None:
      raise WPJApiError(f"Invalid method specified: {method}")
    return True
  
  def get_query_pagination_next(self):
    if self.pagination_end:
      raise WPJApiError(f"All pages have been extracted!")
       
    response = self.get_query()
    items = response.get('items', [])
    
    print(f'Offset: {self._params["offset"]}, size: {len(items)}, hasNextPage: {response.get("hasNextPage", False)}')
    if response.get("hasNextPage", False) != True:
      self.pagination_end = True 

    self._params["offset"] += len(items)
    return items
