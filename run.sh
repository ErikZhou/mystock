#!/bin/bash

#python3 peg.py
#python3 peg.py

MY_MESSAGE=""
echo $MY_MESSAGE
MY_MESSAGE+="python3 peg.py -i output_1.csv"
for (( c=2; c<=44; c++ ))
do  
   #echo "Welcome output_$c.csv times"
    MY_MESSAGE+=" & python3 peg.py -i output_"$c".csv"
done
echo $MY_MESSAGE
$MY_MESSAGE
