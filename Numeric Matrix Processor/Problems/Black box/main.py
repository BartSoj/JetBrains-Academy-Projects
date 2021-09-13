lst_1 = list()
lst_2 = blackbox(lst_1)
print("modifies" if lst_1 is lst_2 else "new")
