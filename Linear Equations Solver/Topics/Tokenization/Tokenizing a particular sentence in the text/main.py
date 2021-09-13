from nltk.tokenize import regexp_tokenize, sent_tokenize

sent = sent_tokenize(input())[int(input())]
print(regexp_tokenize(sent, "[A-z']+"))
