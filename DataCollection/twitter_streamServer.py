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
access_token = "3192478960-BKA4l4m8FtnIHxezJxSzRUUZVvur4beNFwiGfat"
access_token_secret = "MSjqakVrhEFHt2io9yWRdZDtYDRaKnaDPIu8XpQ9ZbUzT"
consumer_key = "DED0mJH6TQO96pd6KzTauqRBd"
consumer_secret = "6f9bIvX5ZoDBWUmyNg4YbBqEhos8SYhLSRExiqdqjHrGAdq02g"


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
    f = open("../keywordshortlist.txt",'rt')
    for line in f:
        array.append(line.replace(',\n',''))
        #print line.replace(',\n','').split(',') splitted in arrays
        # mit dieser Variante pro Zeile ein Keyword ohne hochkomma, jede Zeile mit komma abschliessen
        # und enter, letzte zeile muss leer sein.
        #print line.replace(',\n','')
    print array


    stream.filter(track=array,languages=['en'])
    #stream.filter(track=["FCBayern","Gunners","Lewandowski"],languages=['en'])

    #finally:
    #f.close()

