FROM ubuntu:22.04

RUN apt update && apt install openssh-server -y
RUN useradd -rm -d /home/geralt -s /bin/bash -u 1000 geralt
RUN echo 'geralt:basketball' | chpasswd # CHANGE THIS PASSWORD YOU BAFFOON
RUN service ssh start

COPY flag.txt /home/geralt/flag.txt

EXPOSE 22

ENTRYPOINT ["/usr/sbin/sshd", "-D"]