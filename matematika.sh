#!/bin/bash 
#3. piemērs - operacijas ar mainīgajiem
a=56
b=32
val6=`expr $a + $b`
echo "$a + $b = " $val6 
val7=`expr $a - $b`
echo "$a - $b = " $val7 
val8=`expr $a \* $b`
echo "$a * $b = " $val8 
val9=`expr $a / $b`
echo "$a / $b = " $val9 
val10=`expr $a % $b`
echo "$a % $b = " $val10 
 


#2. piemērs - operācijas ar konstantēm
: <<'END'
val1=`expr 2 + 3`
echo "2 + 3 = " $val1 
val1=`expr 2 + 3`
echo "2 + 3 = " $val1 
val2=`expr 2 - 3`
echo "2 - 3 = " $val2 
val3=`expr 2 \* 3`
echo "2 * 3 = "$val3 
val4=`expr 2 / 3`
echo "2 / 3 = "$val4 
val5=`expr 2 % 3`
echo " 2 % 3 = "$val5 "-atlikums no dalijuma"
END
#1. piemērs - izteiksmes pieraksts
: <<'END' #komentara bloka sakums
val=`expr 2 + 2`
echo $val "\` zīmes, ir jābūt atstarpēm"
END
 #komentara bloka beigas


