# fuente: https://towardsdatascience.com/calculating-string-similarity-in-python-276e18a7d33a

import Levenshtein as lev

import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

stopwords = stopwords.words('english')

# if needed
# >>> import nltk
# >>> nltk.download('stopwords')


# Levenshtein method
t = lev.distance('Levenshtein Distance', 'Levensthein Distance')
# print (t)

# Cosine similarity

sentences = [
	'This is a foo bar sentence.',
	'This sentence is similar to a foo bar sentence.',
	'This is another string, but it is not quite similar to the previous ones.',
	'I am just another string.'
]

def clean_string(text):
	text = ''.join([word for word in text if word not in string.punctuation])
	text = text.lower()
	text = ' '.join([word for word in text.split() if word not in stopwords])
	return text

cleaned = list(map(clean_string, sentences))
#cleaned

vectorizer = CountVectorizer().fit_transform(cleaned)
vectors = vectorizer.toarray()
vectors

csim = cosine_similarity(vectors)
csim

def cosine_sim_vectors(vec1, vec2):
	vec1 = vec1.reshape(1, -1)
	vec2 = vec2.reshape(1, -1)
	return cosine_similarity(vec1, vec2)[0][0]

cosine_sim_vectors(vectors[0], vectors[1])


