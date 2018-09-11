#!/bin/bash

ADVANCE=$1

M=`date +%m`

M_ADV=`expr $M + $ADVANCE`

Y=`date +%Y`

if [ $M_ADV -gt 12 ]
then

	M_ADV=`expr $M_ADV - 12`

	Y_ADV=`expr $Y + 1`

	cal -m $M_ADV $Y_ADV | sed 's/^//'

elif [ $M_ADV -le 0 ]
then 
	
	M_ADV=`expr 12 + $M + $ADVANCE`
	
	Y_ADV=`expr $Y - 1`
	
	cal -m $M_ADV $Y_ADV | sed 's/^//'

else

	cal -m $M_ADV $Y | sed 's/^//'

fi
