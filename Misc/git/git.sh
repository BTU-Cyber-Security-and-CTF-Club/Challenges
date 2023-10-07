#!/usr/bin/bash

#script for the .git challenge
cd /tmp/git

git config --global user.name "haxxor"

git config --global user.email "haxxor@hakkerland.com" 

git init

echo "sth" > hello.txt

git add hello.txt

git commit -m "added hello.txt"

rm hello.txt

git commit -m "fix"

echo 'Did you think it was gonna be this easy?' > README.md

git add README.md

git commit -m "Update README.md"

git branch -m secret

git commit -m "created new branch secret"

git tag v1.0.0

git branch secret

git checkout secret

echo "BTU{exp0s3d_g1t_r3po}" > flag.txt

git add flag.txt

git commit -m "added flag.txt"

rm flag.txt

git commit -m "removed flag.txt"

git branch master

git checkout master

echo '<?php echo "Hello World!" ?>' > test.php

git add test.php

git commit -m "added test.php"

git branch main

git checkout main

echo -e '#!'"/bin/bash\n\ntail -f /dev/null" > bitcoinminer.sh

git add bitcoinminer.sh

git commit -m "added script to mine coinz"

git tag "BTU{n0th1ng_t0_s33_h3r3}"

cd $OLDPWD
