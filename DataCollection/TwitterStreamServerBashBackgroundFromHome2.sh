#!/bin/sh

#cd /home/sportvm/Desktop/TwitterStreamServer_4oauth1
#und dann unten die paths weg machen, falls file nicht in twitterstreamserver2 angelegt wird


cd /home/sportvm/Desktop/TwitterStreamServer_4oauth1
cd Data2
now=$(date +"%d_%m_%Y_%H_%M_%S")
newFile2="TwitterData2-$now.txt"
touch $newFile2

# python /home/sportvm/Desktop/TwitterStreamServer_2/twitter_streamServer.py > $newFile
python ../twitter_streamServer_2.py > $newFile2
cd ~

#/home/sportvm/Desktop/TwitterStreamServer_2/TwitterStreamServerBashBackgroundFromHome.sh
#/home/sportvm/Desktop/TwitterStreamServer_4oauth1/TwitterStreamServerBashBackgroundFromHome.sh &
#(pkill TwitterS".";pkill pytho".";(/home/sportvm/Desktop/TwitterStreamServer_4oauth1/TwitterStreamServerBashBackgroundFromHome.sh &))
#(pkill TwitterS".";pkill pytho".";(/home/sportvm/Desktop/TwitterStreamServer_4oauth1/TwitterStreamServerBashBackgroundFromHomeOtherFilestructure.sh &))