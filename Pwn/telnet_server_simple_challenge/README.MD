# Telnet Server Simple Challenge

users can simply login with username "admin" and password "admin" to grab the flag via the motd file. they can e.g. bruteforce this login.
they do not get a real shell, since the login shell of the user "admin" is `/sbin/nologin`
the telnet server is running on tcp port 23. we could also set the port to sth else, to spice it up a little.

## how to run it

`docker build -t telnet_challenge . && docker run --rm -it --name telnet_challenge -p 127.0.0.1:23:23 telnet_challenge`

