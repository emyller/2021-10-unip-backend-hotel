FROM python:3.9
WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
