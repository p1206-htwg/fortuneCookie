#!/bin/sh

cd Data
now=$(date +"%d_%m_%Y_%H_%M_%S")
newFile="TwitterData-$now.txt"
touch $newFile
python ../twitter_streamServer.py > $newFile
cd ..
#con-Befehle:

#*/10 * * * * /usr/bin/sh TwitterStreamWithBash.sh
#zum beenden:
#*/10 * * * * /usr/bin/sh killall -9 TwitterStreamWithBash.sh
#

#fg %1
#^C
#oder Steuerung C
#oder
#kill %1

#/home/sportvm/Desktop/TwitterStreamServer_2/TwitterStreamIntoFileBash.sh
#/home/sportvm/Desktop/TwitterStreamServer_2/TwitterStreamIntoFileBash.sh &
#.//home/sportvm/Desktop/TwitterStreamServer_2/TwitterStreamIntoFileBash.sh &
#.//home/sportvm/Desktop/TwitterStreamServer_2/TwitterStreamIntoFileBash.sh
#./home/sportvm/Desktop/TwitterStreamServer_2/TwitterStreamIntoFileBash.sh
#Ausführen vom ~Verzeichnis:
#/home/sportvm/Desktop/TwitterStreamServer_2/TwitterStreamIntoFileBash.sh
