import os
import pprint
from argparse import ArgumentParser
from apiclient.discovery import build
from google.cloud import bigquery
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')


def main(viewId, table, dateRange):

if __name__ == '__main__':
