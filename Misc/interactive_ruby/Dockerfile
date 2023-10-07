FROM ruby:alpine3.18

RUN apk update && apk upgrade --available && apk add --upgrade socat bash

# Create a group and user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup -h /home/appuser -s irb

RUN echo 'BTU{1s_ruby_fun_0r_n0t?}' > /home/appuser/flag.txt

USER appuser

#https://serverfault.com/questions/1070714/socat-is-it-possible
#https://superuser.com/questions/123790/socat-and-rich-terminals-with-ctrlc-ctrlz-ctrld-propagation

# todo: fix socat command (if we even want socat later on)
ENTRYPOINT ["bash","-c", "socat TCP-LISTEN:1337,reuseaddr,fork system:'irb',pty,stderr,setsid,sigint,sane,raw,echo=0"]