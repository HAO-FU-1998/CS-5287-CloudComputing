import os   # need this for popen
import time # for sleep
import json
from kafka import KafkaProducer  # producer of events
from datetime import datetime
import urllib.request as r

# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I have on my local VMs

# acquire the producer
# (you will need to change this to your bootstrap server's IP addr)
producer = KafkaProducer (bootstrap_servers="129.114.25.58:9092",
                          acks=1, api_version=(0,10,1),
                          value_serializer=lambda v: json.dumps(v).encode('utf-8')
                                          )  # wait for leader to write to log

# say we send the contents 100 times after a sleep of 1 sec in between
for i in range (100):

    # get the output of the top command
    #process = os.popen ("top -n 1 -b")

    # read the contents that we wish to send as topic content
    #contents = process.read ()
    # contents = str("test")
    url='http://api.openweathermap.org/data/2.5/weather?q=chongqing&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
    contents=r.urlopen(url).read().decode('utf-8')
    contents=json.loads(contents)

    now = datetime.now()

    current_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    # json data
    data = {
      "timestamp" : current_time,
      "value": contents
    }

    # send the contents under topic utilizations. Note that it expects
    # the contents in bytes so we convert it to bytes.
    #
    # Note that here I am not serializing the contents into JSON or anything
    # as such but just taking the output as received and sending it as bytes
    # You will need to modify it to send a JSON structure, say something
    # like <timestamp, contents of top>
    #
    producer.send ("utilizations", value=data)
    producer.flush ()   # try to empty the sending buffer

    # sleep a second
    time.sleep (1)

# we are done
producer.close ()
