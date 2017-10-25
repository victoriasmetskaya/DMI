#!/bin/bash
echo "ievadi skaili n"
read n
echo -e "$n \t%1 \t%2 \t%3"
k=0
while (( $k <= 9 ))
do
a=`expr $n % 1`
b=`expr $n % 2`
c=`expr $n % 3`
echo -e "$n \t$a \t$b \t$c"
k=`expr $k + 1`
n=`expr $n + 1`
done
