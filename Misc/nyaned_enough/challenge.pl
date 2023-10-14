#!/usr/bin/perl

# disable buffering of stdout and stderr
select STDERR;
$| = 1;
select STDOUT;
$| = 1;

print "d8578edf8458ce06fbc5bb76a58c5ca4\n";
print "your answer?\n";

$line = <STDIN>; 

chomp $line;

# $line holds the input line from the client.
# replace \r that can come via telnet clients
$line =~ s/\r//g;  # Search for \r, replace it with nothing

if ($line =~ m/^qwerty$/) {  
    print "that is correct, here you go:\n";
    sleep(2);
    system('/home/whodis/nyancat/src/nyancat -t -s -I');
}
else {
    print "you sent $line\n";
    print "not correct. good bye.\n"
}