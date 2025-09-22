import argparse
import requests
import socket
import configparser
import sys

config = configparser.ConfigParser()
config.sections()
config.read('settings.conf')

parser = argparse.ArgumentParser(description="Webhawk agent v1.0\nUse this script to make detection on your endpoints.")

parser.add_argument(
    "-l", 
    "--log_file",
    help = "Path to the Apache log file to scan (e.g., ./SAMPLE_DATA/RAW_APACHE_LOGS/access.log.2022-12-22)", 
    required = True
)

args = parser.parse_args()

with open(args.log_file,'r') as f:
    logs=str(f.read())

params = {"hostname":socket.gethostname(),"logs_content":logs,"log_file":args.log_file}

try:
    response=requests.post("http://{}:{}/scan".format(config['WEBHAWK']['server_ip'],config['WEBHAWK']['server_port']),json=params)
    print(response.json())
except:
    print('Not able to reach webhawk service.\nMake sure that your webhawk server is up that that detection service is running.\nExiting..')
    sys.exit(1)