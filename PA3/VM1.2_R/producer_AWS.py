#!/usr/bin/python
# Author: Stephen Rees
# CS4287-5287: Principles of Cloud Computing, Vanderbilt University
#
# Created: Sept 14, 2021
#
# Purpose:
#
#    Learn the use of Kafka Python streaming APIs.
#    In this case, we create a Kafka producer that 
#	 streams continuous messages realtime from 
#	 the CoinCap WSS endpoint
#

from kafka import KafkaProducer  # producer of events
from websocket import create_connection # needed for WSS connection

# acquire the producer
# (you will need to change this to your bootstrap server's IP addr)
#producer = KafkaProducer (bootstrap_servers="129.114.26.118:9092", acks=1)  #Chameleon - wait for leader to write to log
producer = KafkaProducer (bootstrap_servers="54.227.111.8", acks=1) #AWS - wait for leader to write to log

# read the contents that we wish to send as topic content
ws = create_connection("wss://ws.coincap.io/prices?assets=bitcoin,ethereum,cardano,binance-coin,tether")

# permanent loop to continue processing realtime data. May wish to add a graceful exit...
try:
    while True:
        data = ws.recv()
        print(data)
        # send the contents under topic CoinCap. Note that it expects
        # the contents in bytes so we convert it to bytes.
        #
        # The API produces JSON, so hopefully it is sufficient to send this as is
        #
        producer.send ("CoinCap_1-5", value=bytes (data, 'ascii'))
        producer.flush ()   # try to empty the sending buffer
except KeyboardInterrupt:
    pass
# we are done - however without a graceful exit mechanism, this will never run.
producer.close ()
