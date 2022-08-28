
# Purpose:
#
#    Demonstrate the use of Kafka Python streaming APIs.
#    In this example, demonstrate Kafka streaming API to build a consumer.
#

import os   # need this for popen
import time # for sleep
import couchdb
import json
from kafka import KafkaConsumer  # consumer of events
import datetime

# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I have on my local VMs
couch = couchdb.Server('http://user1:123456@129.114.25.58:5984/')
db = couch['pa1']


# acquire the consumer
# (you will need to change this to your bootstrap server's IP addr)
consumer = KafkaConsumer (bootstrap_servers=["129.114.25.15:9092","129.114.25.58:9092"],
                          value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# subscribe to topic
consumer.subscribe (topics=["utilizations"])


#couch = couchdb.Server('http://user1:123456@129.114.25.58:5984/')

#db = None
#try:
#    db = couch.database['cloudpa1']
#except Exception as e:
#    db = couch.create['cloudpa1']
#db = couch['qinzhao_database']

# we keep reading and printing
for msg in consumer:
    # what we get is a record. From this record, we are interested in printing
    # the contents of the value field. We are sure that we get only the
    # utilizations topic because that is the only topic we subscribed to.
    # Otherwise we will need to demultiplex the incoming data according to the
    # topic coming in.
    #
    # convert the value field into string (ASCII)
    #
    # Note that I am not showing code to obtain the incoming data as JSON
    # nor am I showing any code to connect to a backend database sink to
    # dump the incoming data. You will have to do that for the assignment.
    doc = {'created_at': json.dumps(datetime.datetime.now().isoformat()), 'topic': msg.topic, 'value': msg.value}
    db.save(doc)
    print (doc)
    #db.save(msg.value)
    #print (msg.value)

# we are done. As such, we are not going to get here as the above loop
# is a forever loop.
consumer.close ()
    

