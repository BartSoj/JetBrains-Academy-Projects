def xor(a, b):
    return (a if a else b) if bool(a) != bool(b) else False
