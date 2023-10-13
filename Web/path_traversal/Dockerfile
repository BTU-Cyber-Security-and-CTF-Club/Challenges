FROM httpd:2.4.49-alpine

COPY ./public/ /usr/local/apache2/htdocs
COPY httpd.conf /usr/local/apache2/conf/httpd.conf
COPY flag.txt /flag.txt

EXPOSE 80
CMD ["httpd", "-X"]