lib = shelve.open("my_library", writeback=True)
lib["Divergent trilogy"] = ["Divergent", "Insurgent", "	Allegiant"]
lib["The Lord of the Rings"] = ["The Fellowship of the Ring", "The Two Towers", "The Return of the King",
                                "The Silmarillion"]

lib["The Lord of the Rings"].pop(3)

print(len(lib["The Lord of the Rings"]))

lib.close()
