FROM python:3

RUN mkdir ~/setup
run mkdir ~/src
COPY requirements.pip ~/setup

WORKDIR ~/src

RUN pip install --no-cache-dir -r requirements.pip