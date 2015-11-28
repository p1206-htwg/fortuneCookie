tokens= []

def readfile(filename):
	"""read in textfile with tweets"""

	text_file = open(filename, "r")
	tweets_full = text_file.readlines()
	text_file.close()
	return tweets_full

def tokenize(tweets_full):
    """Tokenizes the array tweets_full"""
   
    for tweet in tweets_full:
        tokens.append(tweet.split())
        
        
    for i in tokens:
        for j in i[:]:  
            
            if j.istitle():
                print (j)
                #i.remove(j)
                del i[i.index(j)]
                
                          
                
    return tokens
 
 
 


test= readfile("Tweets.txt")
tokenize(test)

                
print (tokens)



#wenn del, dann wird das wort danach 
#übersprungen, weil alle felder um 1
#dekremntiert werden
#j wird dabei aber
#trotzdem inkrementiert!