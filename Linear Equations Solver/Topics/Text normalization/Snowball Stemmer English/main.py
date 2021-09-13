from nltk.stem import SnowballStemmer

# the following line reads a text from the input and converts it into a list
sent = input().split()

stemmer = SnowballStemmer(language="english")

for w in sent:
    print(stemmer.stem(w))
