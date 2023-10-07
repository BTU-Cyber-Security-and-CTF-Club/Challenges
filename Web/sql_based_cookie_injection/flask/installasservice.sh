#!/bin/bash

# script to run the flask server as a service

# TODO run as non root

groupadd flask
useradd -g flask -s /usr/sbin/nologin -d /home/flask flask

cp -r flask/* /home/flask/
pip3 install -r requirements.txt
cp flask.service /lib/systemd/system/
#chmod 640 /lib/systemd/system/flask.service
systemctl daemon-reload
systemctl enable flask.service
systemctl start flask.service