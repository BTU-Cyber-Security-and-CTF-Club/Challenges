FROM alpine:latest

RUN apk update && apk upgrade --available && apk add --upgrade python3 py-pip bash
RUN addgroup -S appgroup && adduser -S gollum -G appgroup -h /home/gollum -s /sbin/nologin
WORKDIR /home/gollum
RUN mkdir -p mordor && echo "BTU{SMB_1zz_s3cur3?}" > mordor/flag.txt
RUN wget https://raw.githubusercontent.com/fortra/impacket/master/examples/smbserver.py
RUN python3 -m pip install impacket

EXPOSE 445

ENTRYPOINT ["python3", "smbserver.py", "-comment", "'you shall not pass'", "-smb2support", "one_does_not_simply_walk_into_mordor", "/home/gollum/mordor"]
