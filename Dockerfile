FROM python:3.10-alpine
LABEL Maintainer="KevinKien"

WORKDIR /ipinfo

RUN apk update && apk upgrade --no-cache

COPY . /ipinfo/

RUN pip3 install -r requirements.txt --no-cache-dir

CMD python3 runserver.py