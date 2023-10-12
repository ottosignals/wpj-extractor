import os
import datetime

from bigquery.api import BigQueryApi
from wpj.api import WPJApi
from wpj.queries.orders import bq_schema as orders_bq_schema
from wpj.queries.products import bq_schema as products_bq_schema

def run():
  PROJECT_ID = os.environ.get('PROJECT_ID')
  DATASET_ID = os.environ.get('DATASET_ID')
  TABLE_ID = os.environ.get('TABLE_ID')

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
  elif params["numOfDaysUpdated"] > 0:
    filter["dateUpdated"] = {}
    filter["dateUpdated"]["ge"] = datetime.datetime.now() - datetime.timedelta(days=params["numOfDaysUpdated"])
    filter["dateUpdated"]["ge"] =  filter["dateUpdated"]["ge"].replace(hour=0, minute=0, second=0, microsecond=0).isoformat(sep=' ')
    filter["dateUpdated"]["le"] = datetime.datetime.now() 
    filter["dateUpdated"]["le"] =  filter["dateUpdated"]["le"].replace(hour=0, minute=0, second=0, microsecond=0).isoformat(sep=' ')


  api = WPJApi(API_DOMAIN, API_KEY)
  bq = BigQueryApi()
  schema = None
  rows = []
  
  print(f"Downloading data from '{API_DOMAIN}' with method '{API_METHOD}' and filter '{filter}'")
  if API_METHOD == 'orders':
    rows = api.get_query_pagination(API_METHOD, limit=100, sort='{dateCreated: ASC}', filter=filter)
    schema = orders_bq_schema
  elif API_METHOD == 'products':
    rows = api.get_query_pagination(API_METHOD, limit=1000, sort='{id: ASC}')
    schema = products_bq_schema

  print(f"Downloaded '{len(rows)}' rows of data")
  print(f"Inserting downloaded data to BigQuery")
  bq.insert(PROJECT_ID, DATASET_ID, TABLE_ID, rows, schema=schema)
  print(f"Data has been inserted to BigQuery")


run()




