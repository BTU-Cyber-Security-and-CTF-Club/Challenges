FROM php:8.1-apache

# get updates
RUN apt update && \
    apt upgrade -y && \
    apt install -y git bash dos2unix    

WORKDIR /var/www/html

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf 

COPY index.php index.php

COPY 000-default.conf /etc/apache2/sites-available/

RUN mkdir /tmp/git

ADD git.sh /tmp

RUN cd /tmp && dos2unix git.sh && chmod +x git.sh && ./git.sh && cp -r git/* /var/www/html/ && cp -r git/.git /var/www/html/