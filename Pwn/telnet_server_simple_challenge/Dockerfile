FROM alpine:latest

# telnet package is installed via busybox-extras
RUN apk update && apk upgrade --available && apk add --upgrade busybox-extras

# Create a group and user which can not get a "real" login though
RUN addgroup -S appgroup && adduser -S admin -G appgroup -h /home/admin -s /sbin/nologin

# change password; this user can then be logged in with via telnet
RUN echo 'admin:admin' | chpasswd

# we put our message in the message of the day file (this will be shown before /sbin/nologin is executed)
RUN echo -e "\n\nHere you go:\n\n"'BTU{wh4t_1z_t3ln3t}'"\n\n" > /etc/motd

# run telnetd in foreground, on tcp port 23
ENTRYPOINT [ "telnetd", "-p", "23", "-F"]