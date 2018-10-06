
# coding: utf-8

# In[39]:


import bs4 as bs
import urllib.request
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.corpus import stopwords

stop = stopwords.words('english')

source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)').read()
soup = bs.BeautifulSoup(source,'lxml')


text_file = open("input.txt", "w", encoding="utf-8")
for paragraph in soup.find_all('p'):
    text_file.write(str(paragraph.text))
    
f = open('input.txt', encoding="utf-8")
raw = f.read()

tokens = nltk.word_tokenize(raw)
tokens = [token for token in tokens if token not in stop]
tokens = [word for word in tokens if len(word) >= 3]
tokens = [word.lower() for word in tokens]

# print (tokens)

# ----------------------------------------------------------
# Stemming Example

from nltk.stem import PorterStemmer
#
# ps = PorterStemmer()
# for w in tokens:
#     print(ps.stem(w))
#
# ----------------------------------------------------------

# Part of Speech tagging: Example

# print(nltk.pos_tag(tokens))

# --------------------------------------------------------
# Lemmatization Example 

from nltk.stem import WordNetLemmatizer
from nltk.stem import LancasterStemmer
#
lemmatizer = WordNetLemmatizer()
stemmer = LancasterStemmer()
#
# print(stemmer.stem(raw))
# print(lemmatizer.lemmatize(raw))

# ---------------------------------------------------------
# Named Entity Recognition (NER): Example

from nltk import wordpunct_tokenize, pos_tag, ne_chunk
#
# print(ne_chunk(pos_tag(wordpunct_tokenize(raw))))
#
#---------------------------------------------------------

from nltk.util import ngrams

trigrams = ngrams(tokens,3)
print (*trigrams)


