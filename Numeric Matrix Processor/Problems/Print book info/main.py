def print_book_info(title, author=None, year=None):
    res = '"' + title + '"'
    if author or year:
        res += " was written"
        if author:
            res += " by " + author
        if year:
            res += " in " + year
    return print(res)
