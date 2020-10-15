#!/bin/bash

#python3 peg.py
#python3 peg.py

MY_MESSAGE="rm -rf *.csv"
echo $MY_MESSAGE
$MY_MESSAGE

MY_MESSAGE="python mystock.py"
echo $MY_MESSAGE
$MY_MESSAGE

MY_MESSAGE="python pool.py"
echo $MY_MESSAGE
$MY_MESSAGE

MY_MESSAGE="python csv_merge.py"
echo $MY_MESSAGE
$MY_MESSAGE

MY_MESSAGE="python csv_sort.py"
echo $MY_MESSAGE
$MY_MESSAGE


