# interactive ruby

`docker build -t irb . && docker run --rm -it --name irb -p 127.0.0.1:1337:1337 irb`

## how to get the flag

e.g. by connecting with `nc localhost 1337` and then using `exec("cat ~/flag.txt")`

## todos

- restrict what the user "appuser" can do with ruby, if possible, let only a handful of commands work (and not "exec" if possible)
- make serving of irb stable and as pretty as wanted (it is not right now)