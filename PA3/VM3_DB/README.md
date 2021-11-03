Kafka Installation
--
Shell scripts were translated into ansible modules. Followed the same notes from the previous assignment.

CouchDB Installation
--
Shell scripts were translated into ansible modules. Followed the same notes from the previous assignment.


Modifications
--
Kafka and couch are now systemd services that are ran after the server has provisioned, removing the need to manually execute the scripts.

Local Ansible Development
--
I copied VM1.2 files configured for my machine to test VM3's playbooks. 

Check that couchdb is running
```
ssh -i ~/.ssh/my_key.pem ubuntu@db_ip
sudo systemctl status couchdb
http://db_ip:5984/_utils/#
```
