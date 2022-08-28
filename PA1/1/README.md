# Milestone 1

## Import .pem file to enable VM access:
### Chameleon Cloud:

chmod 600 Team7_Chameleon_SSH.pem

ssh-add Team7_Chameleon_SSH.pem

### AWS:

chmod 600 Team7_AWS_SSH.pem

ssh-add Team7_AWS_SSH.pem

## ssh into the instance: 

### VM 2 & 3 (Chameleon)
ssh cc@129.114.25.15

ssh cc@129.114.25.58

### VM 2 & 3 (AWS)
ssh ubuntu@54.242.9.157

ssh ubuntu@54.242.145.238

# Milestone 2

## Start Zookeeper server and Kafka brokers

### VM2 (Both Chameleon and AWS)：
cd kafka_2.13-2.8.0

bin/zookeeper-server-start.sh config/zookeeper.properties

bin/kafka-server-start.sh config/server.properties

### VM3 (Both Chameleon and AWS)：
cd kafka_2.13-2.8.0

bin/zookeeper-server-start.sh config/zookeeper.properties

bin/kafka-server-start.sh config/server.properties --override broker.id=1

## Open another terminal to execute producer.py and consumer.py

### VM2 (Chameleon): 
python3 consumer_cc.py

### VM1.x (Local VM): 
python3 producer_cc.py

# Milestone 3

## Execute producer.py and consumer.py

### VM2 (Chameleon): 
python3 consumer_cc.py

### VM1.x (Local VM): 
python3 producer_cc.py

### VM2 (AWS): 
python3 consumer_aws.py

### VM1.x (Local VM): 
python3 producer_aws.py

## Check the data on the Fauxton web console

### Chameleon Cloud:
http://129.114.25.58:5984/_utils/#database/pa1/_all_docs

### AWS:
http://54.242.145.238:5984/_utils/#database/pa1/_all_docs

# Documentations:
API data: http://api.openweathermap.org/data/2.5/weather?q=chongqing&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996

Source: Openweathermap
