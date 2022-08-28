import csv
import json
import time
import pandas as pd
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="129.114.25.15:30000", acks=1)

header_list = ['id', 'timestamp', 'value', 'property', 'plug_id', 'household_id', 'house_id']
with pd.read_csv('energy.csv', names=header_list, skiprows=0, chunksize=1000) as reader:
    counter = 1
    for chunk in reader:
        print('Send chunk:', counter)
        if counter == 1:
          print(chunk.to_json(orient="records"))
        producer.send("utilization", value=bytes(chunk.to_json(orient="records"),'UTF-8'))
        producer.flush()
        counter += 1
producer.close()
