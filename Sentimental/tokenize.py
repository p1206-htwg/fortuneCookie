from nltk.tokenize import word_tokenize

example = ['Mary had a little lamb' , 'Jack went up the hill' ]

tokenized_sents = [word_tokenize(i) for i in example]
for i in tokenized_sents:
    print i
