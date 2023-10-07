## how to run it

build the docker image and run it:

```docker build -t git_challenge .```

```docker run --rm -it -p 127.0.0.1:80:80 --name git_challenge git_challenge```

On port 80, there is the path /.git accessible.

