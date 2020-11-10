FROM python:3.6-alpine

RUN apk update && apk upgrade \
    && apk add zsh \
    && rm -rf /var/cache/apk/*

ONBUILD ADD app /app/
WORKDIR /app
ENV FLASK_APP ./app/app.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY ./requeriments.txt /app/requeriments.txt
RUN pip install -r requeriments.txt
COPY . /app
CMD [ "flask", "run" ]