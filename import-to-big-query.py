import os
import pprint
from argparse import ArgumentParser
from apiclient.discovery import build
from google.cloud import bigquery
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')


def generateInserts(clientId, activities):
  inserts = []
  for activity in activities:
    inserts.append(f"""(
    "{clientId}",
    "{activity['activityTime']}",
    "{activity['activityType']}",
    "{activity['campaign']}",
    "{activity['channelGrouping']}",
    "{activity['hostname']}",
    "{activity['keyword']}",
    "{activity['landingPagePath']}",
    "{activity['medium']}",
    ["{activity['pageview']['pagePath']}"],
    "{activity['source']}")
    """)
  return inserts

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
