import requests
import socket

with open("./SAMPLE_DATA/RAW_APACHE_LOGS/access.log.2017-05-24_small",'r') as f:
    logs=str(f.read())

params = {"hostname":socket.gethostname(),"logs_content":logs}
response=requests.post("http://127.0.0.1:8000/scan",json=params)
print(response.json())