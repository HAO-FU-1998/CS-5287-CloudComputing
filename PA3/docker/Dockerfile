# Author: Morley Bankston
# Vanderbilt University
#
# Consumer Image

FROM python:3.7-alpine

# Now install the needed python packages
RUN apk add --update && apk add net-tools python3 gcc
RUN apk add --no-cache python3 py3-pip
RUN pip3 install kafka-python
WORKDIR /home/ubuntu/CS5287/common
COPY . .

ENV FLASK_APP=app.py
CMD ["python3", "consumer.py"]