#http://www.bogotobogo.com/python/NLTK/Stemming_NLTK.php
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer 

def get_tokens():
	with open('stem_sample.txt') as stem:
		tokens = nltk.word_tokenize(stem.read())
	return tokens

def do_stemming(filtered):
	stemmed = []
	for f in filtered:
		stemmed.append(PorterStemmer().stem(f))
		#stemmed.append(LancasterStemmer().stem(f))
		#stemmed.append(SnowballStemmer('english').stem(f))
	return stemmed

if __name__ == "__main__":

	tokens = get_tokens()
	print("tokens = {}".format(tokens))
	
	stemmed_tokens = do_stemming(tokens)
	print("stemmed_tokens = {}".format(stemmed_tokens))

	result = dict(zip(tokens, stemmed_tokens))
	print("{tokens:stemmed} = ",result)