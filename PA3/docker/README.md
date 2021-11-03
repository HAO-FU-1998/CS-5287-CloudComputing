run docker compose
`cd docker`
`sudo docker-compose -f vm3-compose.yml up -d`
`sudo docker-compose -f vm2-compose.yml up -d`

Notes:
Consumer will build it's image from the Dockerfile

todo:
- ansible will need to write the dynamic host ips to the .env file

Teardown containers
`sudo docker stop $(sudo docker ps -a -q)`

Remove images
`sudo docker rm $(sudo docker ps -a -q)`

