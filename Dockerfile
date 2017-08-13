FROM alpine:latest

RUN apk update && apk upgrade
RUN apk add --upgrade python
RUN apk add --upgrade py-pip
ADD requirements.pip /etc

RUN mkdir ~/src
WORKDIR ~/src