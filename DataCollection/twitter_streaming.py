#!/usr/bin/env python
# encoding=utf8
import sys
import csv
#import scrypt
import codecs



reload(sys)
sys.setdefaultencoding('utf8')
# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream




# Variables that contains the user credentials to access Twitter API
access_token = "3906124394-LlgsoHG80ic6i3riOupm5iytk7Uq5AiKx5HFSqb"
access_token_secret = "2wSHn3BuKCQJxYDJ75zjFEP7s8E8WV7lrsNYhf219IHIG"
consumer_key = "xTmS3DJyRbtSpAXMQj35fjo24"
consumer_secret = "6QYvU5tXVLoD7gw7NIXiR9VNH4CMmMZ56hvIr5a54U2GsFQ7pZ"


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
       # f = open('out9.txt', 'w')
        #data >> f #, 'Filename:', filename  # or f.write('...\n')
        #f.write(data)
        #f.write(data + '\n')
        #f.write(data)
        #print >>f, data + '\n'
        #f.close()
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    # This handles Twitter authentification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    # This line filter Twitter Streams to capture data by the keywords: 'FcBayern', 'ManUtd', 'PremiereLeague'

    #f = open("keywordlist.txt",'rt')
    #items=f.readline()

    #print items
    #print type(items)

    array=[]
    f = open("keywordlist.txt",'rt')
    for line in f:
        array.append(line.replace(',\n',''))
        #print line.replace(',\n','').split(',') splitted in arrays
        # mit dieser Variante pro Zeile ein Keyword ohne hochkomma, jede Zeile mit komma abschliessen
        # und enter, letzte zeile muss leer sein.
        print line.replace(',\n','')
    print array


    stream.filter(track=array,languages=['en'])
    #stream.filter(track=["FCBayern","Gunners","Lewandowski"],languages=['en'])

    #finally:
        #f.close()

