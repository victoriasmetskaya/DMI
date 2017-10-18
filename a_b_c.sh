#!/bin/bash
echo "ievadi tris skaitlus"
read a b c 

if [ $a -gt $b ]
then
	if [ $a -gt $c ]
	then
		if [ $b -gt $c ]
		then
		pirmais=$c
		otrais=$b
		tresais=$a
		else
		pirmais=$b
		otrais=$c
		tresais=$a
		fi
	else 
	pirmais=$b
	otrais=$a
	tresais=$c
  	fi
elif [ $b -gt $c ]
	then
	if [ $a -gt $c ]
	then
	pirmais=$c
	otrais=$a
	tresais=$b
	else
	pirmais=$a
	otrais=$c
	tresais=$b
  	fi	
else
pirmais=$a
otrais=$b
tresais=$c
fi
echo $pirmais $otrais $tresais

#3. tris skailu salidzinasana
:<<'END'
echo "ievadi a"
read a
echo "ievadi b"
read b
echo "ievadi c"
read c

if [ $a -gt $b ]
then
  if [ $a -gt $c ]
  then
  echo  "a "$a " vislielakais"
  elif [ $b -gt $c ]
  then 
  echo "b "$b " vislielakais"
  else
 echo "c "$c " vislielakais"
  fi
elif [ $b -gt $c ]
then 
echo "b "$b "vislielakais"
else
echo "c "$c "vislielakais"
fi
END

#2. divu skailtu salidzinasana 
:<<'END'
echo "ievadi a"
read a
echo "ievadi b"
read b
if [ $a -eq $b ]
then
echo "a = b"
elif [ $a -gt $b ]
then
echo "a > b"
else
echo "a < b"
fi
END
#1. divu skaitlu salidzinasana
:<<'END'
echo "ievadi a"
read a
echo "ievadi b"
read b
if [ $a -gt $b ]
then
echo "a lielaks par b"
else 
echo "a nav lielaks par b"
fi 
END

