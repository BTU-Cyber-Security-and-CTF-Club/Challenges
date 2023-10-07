FROM mysql:5.7.37-debian

# TODO: run as non privileged user and get updates

# sql file to setup the database
COPY setupcommands.sql /docker-entrypoint-initdb.d/
