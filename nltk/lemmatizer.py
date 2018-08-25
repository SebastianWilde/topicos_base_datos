#https://textminingonline.com/dive-into-nltk-part-iv-stemming-and-lemmatization
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
lemma = wordnet_lemmatizer.lemmatize('dogs')
print(lemma)