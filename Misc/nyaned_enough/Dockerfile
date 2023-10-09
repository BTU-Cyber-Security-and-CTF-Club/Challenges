FROM debian:latest

RUN apt update && apt upgrade -y && apt install -y git build-essential socat

RUN useradd -ms /bin/bash whodis

USER whodis

WORKDIR /home/whodis

RUN git clone https://github.com/klange/nyancat.git

# display the flag every 10th second; replace with sed; we have to escape all "\" and "[" characters with another "\", otherwise the sed command fails
RUN cd nyancat && sed -i 's+printf("\\033\[1;37mYou have nyaned for %0.0f seconds!\\033\[J\\033\[0m", diff);+if ((int) diff % 10 == 0 ){printf("\\033\[1;37mBTU{y0u_h4v3_ny4n3d_3n0ugh}\\033\[J\\033\[0m");} else {printf("\\033\[1;37mYou have nyaned for %0.0f seconds!\\033\[J\\033\[0m", diff);}+g' src/nyancat.c

RUN cd nyancat && make

COPY challenge.pl ./

EXPOSE 8080

ENTRYPOINT [ "bash", "-c", "socat TCP-LISTEN:8080,reuseaddr,fork system:'perl challenge.pl',pty,stderr,setsid,sigint,sane,raw,echo=0" ]