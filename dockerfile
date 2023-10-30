FROM python:3.12.0-slim
WORKDIR /usr/flask-redis-app/
COPY ./ ./

RUN apt update
RUN apt-get -y install python3-dev build-essential redis-server
RUN pip install poetry==1.5.1
RUN poetry install