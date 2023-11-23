import os
import datetime

from bigquery.api import BigQueryApi, WriteDisposition
from wpj.api import WPJApi
from wpj.queries.orders import bq_schema as orders_bq_schema
from wpj.queries.products import bq_schema as products_bq_schema
from wpj.queries.sales import bq_schema as sales_bq_schema
from wpj.queries.users import bq_schema as users_bq_schema

def run():
  PROJECT_ID = os.environ.get('PROJECT_ID')
  DATASET_ID = os.environ.get('DATASET_ID')
  TABLE_ID = os.environ.get('TABLE_ID')
  TABLE_WRITE_METHOD = os.environ.get("TABLE_WRITE_DISPOSITION", WriteDisposition.WRITE_APPEND)
  if TABLE_WRITE_METHOD not in WriteDisposition.__dict__.keys():
    TABLE_WRITE_METHOD = WriteDisposition.WRITE_APPEND

  API_KEY = os.getenv("API_KEY")
  API_DOMAIN = os.getenv("API_DOMAIN")
  API_METHOD = os.getenv("API_METHOD")
  
  params = {
    "dateFrom": os.environ.get('date_from'),
    "dateTo": os.environ.get('date_to')
  }

  try:
    params['numOfDays'] = int(os.environ.get('num_of_days', 0))
  except ValueError:
    params['numOfDays'] = 0

  try:
    params['numOfDaysCreated'] = int(os.environ.get('num_of_days_created', 0))
  except ValueError:
    params['numOfDaysCreated'] = 0

  try:
    params['numOfDaysUpdated'] = int(os.environ.get('num_of_days_updated', 3))
  except ValueError:
    params['numOfDaysUpdated'] = 3

  filter = {}
  if params["dateFrom"]:
    filter["dateFrom"] = datetime.datetime.strptime(params["dateFrom"], '%Y-%m-%d').isoformat(sep=' ')
    filter["dateTo"] = datetime.datetime.strptime(params["dateTo"], '%Y-%m-%d').isoformat(sep=' ') 
  elif params["numOfDays"] > 0:
    filter["dateFrom"] = datetime.datetime.now() - datetime.timedelta(days=params["numOfDays"])
    filter["dateFrom"] = filter["dateFrom"].replace(hour=0, minute=0, second=0, microsecond=0).isoformat(sep=' ')
    filter["dateTo"] = datetime.datetime.now() 
    filter["dateTo"] = filter["dateTo"].replace(hour=0, minute=0, second=0, microsecond=0).isoformat(sep=' ')
  elif params["numOfDaysCreated"] > 0:
    filter["dateCreated"] = {}
    filter["dateCreated"]["ge"] = datetime.datetime.now() - datetime.timedelta(days=params["numOfDaysCreated"])
    filter["dateCreated"]["ge"] =  filter["dateCreated"]["ge"].replace(hour=0, minute=0, second=0, microsecond=0).isoformat(sep=' ')
    filter["dateCreated"]["le"] = datetime.datetime.now() 
    filter["dateCreated"]["le"] =  filter["dateCreated"]["le"].replace(hour=0, minute=0, second=0, microsecond=0).isoformat(sep=' ')
  elif params["numOfDaysUpdated"] > 0:
    filter["dateUpdated"] = {}
    filter["dateUpdated"]["ge"] = datetime.datetime.now() - datetime.timedelta(days=params["numOfDaysUpdated"])
    filter["dateUpdated"]["ge"] =  filter["dateUpdated"]["ge"].replace(hour=0, minute=0, second=0, microsecond=0).isoformat(sep=' ')
    filter["dateUpdated"]["le"] = datetime.datetime.now() 
    filter["dateUpdated"]["le"] =  filter["dateUpdated"]["le"].replace(hour=0, minute=0, second=0, microsecond=0).isoformat(sep=' ')


  api = WPJApi(API_DOMAIN, API_KEY)
  bq = BigQueryApi(write_method=TABLE_WRITE_METHOD)
  schema = None
  rows = []
  
  if API_METHOD == 'orders':
    api.get_query_pagination_init(API_METHOD, limit=100, sort='{dateCreated: ASC}', filter=filter)
    schema = orders_bq_schema
  elif API_METHOD == 'products':
    api.get_query_pagination_init(API_METHOD, limit=500, sort='{id: ASC}')
    schema = products_bq_schema
  elif API_METHOD == 'sales':
    api.get_query_pagination_init(API_METHOD, limit=500, sort='{dateCreated: ASC}', filter=filter)
    schema = sales_bq_schema
  elif API_METHOD == 'users':
    api.get_query_pagination_init(API_METHOD, limit=500)
    schema = users_bq_schema
  
  while api.pagination_end is not True:
    print(f"Downloading data from '{API_DOMAIN}' with method '{API_METHOD}' and filter '{filter}'")
    rows = api.get_query_pagination_next()
    print(f"Downloaded '{len(rows)}' rows of data")
    print(f"Inserting downloaded data to BigQuery")
    bq.insert(PROJECT_ID, DATASET_ID, TABLE_ID, rows, schema=schema)
    print(f"Data has been inserted to BigQuery")


run()




