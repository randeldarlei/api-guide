import pymysql
import sys
import boto3
import os

ENDPOINT=""
PORT=""
USER=""
REGION=""
DBNAME=""
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN']

#gets the credentials drom .aws/credentials
session = boto3.Session(profile_name='default')
client = session.client('rds')

token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

try:
    conn = pymysql.connect(host=ENDPOINT, user=USER, passwd=token, port=PORT, database=DBNAME, ssl_ca='SSLCERTIFICATE')
    cur = conn.cursos()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection faild due to {}".format(e))