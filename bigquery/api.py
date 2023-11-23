from google.cloud import bigquery
from google.cloud.bigquery import WriteDisposition
from google.api_core.exceptions import BadRequest

class BigQueryApi():
  def __init__(self, write_method=WriteDisposition.WRITE_APPEND):
    self._client = bigquery.Client()
    self._write_disposition = write_method

  def insert(self, 
             project, 
             dataset, 
             table, 
             rows, 
             time_partitioning=None, 
             schema=None,
             batch_size=1000000):
    
    dataset_id = bigquery.Dataset(f"{project}.{dataset}")
    dataset_id.location = 'EU'
    self._client.create_dataset(dataset_id, exists_ok=True)

    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = self._write_disposition
    if time_partitioning:
      job_config.time_partitioning = time_partitioning
    if schema:
        job_config.schema = schema
    # job_config.ignore_unknown_values = True

    table_id = f"{project}.{dataset}.{table}"
    
    # Split the rows into smaller batches
    for i in range(0, len(rows), batch_size):
      batch = rows[i:i + batch_size]
      job = self._client.load_table_from_json(
        batch, table_id, job_config=job_config
      )
      self._write_disposition = WriteDisposition.WRITE_APPEND

      try:
        job.result()
      except BadRequest as e:
        for e in job.errors:
          print(f"BigQuery error: {e['message']}")
          raise Exception("BigQuery error")
      
