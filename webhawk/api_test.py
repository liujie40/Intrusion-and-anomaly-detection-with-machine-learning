import argparse
import requests
import socket

parser = argparse.ArgumentParser(description="Testing webhawk API with an Apache log file")

parser.add_argument(
    "-l", 
    "--log_file",
    help = "Path to the Apache log file to scan (e.g., ./SAMPLE_DATA/RAW_APACHE_LOGS/access.log.2022-12-22)", 
    required = True
)

args = parser.parse_args()

with open(args.log_file,'r') as f:
    logs=str(f.read())

params = {"hostname":socket.gethostname(),"logs_content":logs}
response=requests.post("http://127.0.0.1:8000/scan",json=params)

print(response.json())
