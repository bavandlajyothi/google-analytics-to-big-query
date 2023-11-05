import os
import pprint
from argparse import ArgumentParser
from apiclient.discovery import build
from google.cloud import bigquery
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')



def getUserActivity(analytics, viewId, userId, dateRange):
  return analytics.userActivity().search(
    body={
      "dateRange": dateRange,
      "viewId": viewId,
      "user": {'type': 'CLIENT_ID', 'userId': userId}
    }
  ).execute()


def extractClientIds(response):
  clientIds = []
  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
    for row in report.get('data', {}).get('rows', []):
      dimensions = row.get('dimensions', [])
      for header, dimension in zip(dimensionHeaders, dimensions):
        if header == 'ga:clientId':
          clientIds.append(dimension)
  return clientIds

def extractActivities(response):
  activities = []

  for session in response.get('sessions', []):
    for activity in session.get('activities', []):
      activities.append(activity)
  return activities

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
