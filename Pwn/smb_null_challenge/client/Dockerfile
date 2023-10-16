FROM debian:latest

RUN apt update && apt upgrade -y && apt install -y smbclient

ENTRYPOINT [ "bash", "-c", "sleep 5 && smbclient -N -L //smb_server" ]