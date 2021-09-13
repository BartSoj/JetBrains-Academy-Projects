from nltk.stem import WordNetLemmatizer

word = input()
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize(word, "n"))
print(lemmatizer.lemmatize(word, "a"))
print(lemmatizer.lemmatize(word, "v"))
