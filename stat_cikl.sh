#!/bin/bash
echo "ievadi skaitlu skaitu"
read n
for (( i=1; i<=n; i++))
do 
echo "ievadi skaitli" 
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
echo "videja vertiba  $vid.$p"
echo "minimala vertiba $min"
echo "maksimala vertiba $max"

