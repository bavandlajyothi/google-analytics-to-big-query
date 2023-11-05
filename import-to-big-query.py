import os
import pprint
from argparse import ArgumentParser
from apiclient.discovery import build
from google.cloud import bigquery
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')


def createTable(table):
  query = f"""CREATE TABLE `{table}` (
  client_id STRING NOT NULL,
  activity_time STRING,
  activity_type STRING,
  campaign STRING,
  channel_grouping STRING,
  hostname STRING,
  keyword STRING,
  landing_page STRING,
  medium STRING,
  page_view ARRAY<STRING>,
  source STRING)
  """
  r = bq.query(query)
  print(r.result())


def main(viewId, table, dateRange):

if __name__ == '__main__':
