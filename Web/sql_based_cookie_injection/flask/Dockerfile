FROM python:3.7-buster

# still todo: add user and group with lowest privileges possible and run the container with that!

# for production, we have to use a production server, in contrast to the CMD seen below

# get updates
RUN apt update && \
    apt upgrade -y

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

ADD static /app/static

ADD templates /app/templates

COPY server.py /app/

CMD [ "/bin/bash", "-c", "export FLASK_APP=server.py && flask run --host=0.0.0.0 -p 8080" ]