#!/bin/bash
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

