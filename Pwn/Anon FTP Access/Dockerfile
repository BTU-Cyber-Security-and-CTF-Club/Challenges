FROM debian:12.1-slim

RUN apt update && apt install -y vsftpd
COPY vsftpd.conf /etc/vsftpd.conf
RUN mkdir /app
RUN mkdir -p /var/run/vsftpd/empty
COPY flag.txt /app/flag.txt
RUN chmod 744 /app/flag.txt
EXPOSE 21 20
CMD ["vsftpd"]