# Nyaned enough

players have to connect to TCP port 8080 with either e.g. netcat, telnet or sth. similar. They have to respond with the correct answer to the origin of the provided md5 hash.

if they get the answer right, they are greeted by a nyancat cli, every 10th second the flag is displayed in there.

## how to run it

`docker build -t nyaned_enough . && docker run --rm -it --name nyan -p 127.0.0.1:8080:8080 nyaned_enough`

then connect e.g. with

`nc localhost 8080`