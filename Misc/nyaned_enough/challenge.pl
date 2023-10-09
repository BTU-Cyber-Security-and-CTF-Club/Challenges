#!/usr/bin/perl

# disable buffering of stdout and stderr
select STDERR;
$| = 1;
select STDOUT;
$| = 1;

print "5badcaf789d3d1d09794d8f021f40f0e\n";
print "your answer?\n";

$line = <STDIN>; 

chomp $line;

# 5badcaf789d3d1d09794d8f021f40f0e is the md5 of the word "starwars"

# $line holds the input line from the client.
# replace \r\n or \r that can come via telnet clients
$line =~ s/\r\n/\n/g;  # Search for \r\n, replace it with \n
$line =~ s/\r/\n/g;  # Search for \r, replace it with \n

if ($line =~ m/^starwars$/) {  
    print "that is correct, here you go:\n";
    sleep(2);
    system('/home/whodis/nyancat/src/nyancat -t -s -I');
}
else {
    print "you sent $line\n";
    print "not correct. good bye.\n"
}