#!/bin/sh
# This file is based on a piece of code from "Movie Thumnailer".
# See Licenses for more info
# Thanks to Starl1te for its great work.
# Usage: Copisterio_mt PATH_TO_MOVIE PATH_TO_THUMBS/NAME_OF_THUMB PATH_TO_MOVIES

[[ -e /etc/copisterio/mt.config ]] && . /etc/copisterio/mt.config || echo -e "Logs wont be saved"
[[ $1 ]] && echo "No args provided. Quitting"; exit

l="`mplayer -identify "$1" -frames 1 -ao null -vo null 2>/dev/null | grep LENGTH | sed -e 's/^.*=//' -e 's/[.].*//'`"
if [ "$l" =! '' ]; then 
	if [ $LOGDIR ];	then echo "Couldn't identify file $file" >> $LOGDIR/$LOGFILE;fi
else 
	echo "Couldn't identify file $file"; exit; fi

st=`echo $[$l/3/60]`
mkdir tmp

for i in `seq 1 3`; do
	r=$RANDOM; let "r %= 25"
	cd tmp && \
	mplayer -ss `echo $[$st*60*$i+$r]` -noautosub -frames 1 -ao null\
	 -vo png "$1" > /dev/null 2>&1
	cd ..
	mv tmp/*1.png "$2-$i.png"
done

mv "$1" "$3"; 
