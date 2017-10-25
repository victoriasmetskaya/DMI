#!/bin/bash
echo "n"
read n
for (( i=1; i<=n; i++))
do 
echo "x" 
read x
sum=`expr $sum + $x`

if (( i==1 ))
then
max=$x
min=$x
elif (( $x > $max ))
then
max=$x
elif (( $x < $min ))
then
min=$x 
fi
done
vid=`expr $sum / $n` 
atl=`expr $sum % $n`
p=`expr $atl \* 10 / $n`
echo "vid $vid.$p"
echo "min $min"
echo "max $max"
for (( j=1; j<=n; j++ ))
do
if (( $x != $min ))
then 
min2$j=$x
	if (( $min2$j < $x ))
then
