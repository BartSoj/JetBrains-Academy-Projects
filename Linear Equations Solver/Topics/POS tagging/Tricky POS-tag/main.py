import nltk

sent = ['The', 'horse', 'that', 'was', 'raced', 'past', 'the', 'barn', 'fell', 'down', '.']
tag_sent = nltk.pos_tag(sent)
print(tag_sent[4][1])
