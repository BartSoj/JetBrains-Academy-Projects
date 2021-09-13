def tallest_people(**kwargs):
    tallest = max(kwargs.values())
    for key, val in sorted(kwargs.items()):
        if val == tallest:
            print(key + " : " + str(val))
