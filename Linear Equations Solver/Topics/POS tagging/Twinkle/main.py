import nltk

poem = ['Twinkle', ',', 'twinkle', ',', 'little', 'star', ',',
        'How', 'I', 'wonder', 'what', 'you', 'are', '.',
        'Up', 'above', 'the', 'world', 'so', 'high', ',',
        'Like', 'a', 'diamond', 'in', 'the', 'sky', '.']

# in one line
[print(val[0]) for val in nltk.pos_tag(poem) if val[1] == "NN"]
# or
# print("\n".join(map(lambda x: x[0], filter(lambda x: x[1] == "NN", nltk.pos_tag(poem)))))
