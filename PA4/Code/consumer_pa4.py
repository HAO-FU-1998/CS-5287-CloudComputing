import os
import time
import couchdb
import json
import requests
from kafka import KafkaConsumer
from datetime import datetime

couch = couchdb.Server('http://admin:123456@129.114.25.15:30005/')
dbname = "cloudpa4"
db = couch[dbname]

consumer = KafkaConsumer (bootstrap_servers=["129.114.25.15:30000", "129.114.25.15:30001"],
                          value_deserializer=lambda m: json.loads(m.decode('utf-8')))

consumer.subscribe (topics=["utilization"])
    
try: 
    counter = 1
    for msg in consumer:
        print(msg.topic, f'==== received chunk {counter} =====')
        print('=== item ====', msg.value[0])
        url = 'http://admin:123456@129.114.25.15:30005/cloudpa4/_bulk_docs'
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        docs = json.dumps({'docs': msg.value})
        res2 = requests.post(url, headers=headers, data=docs)
        print('==== send data to couch results ====', res2.content)
        counter += 1
except KeyboardInterrupt:
    pass
consumer.close ()

