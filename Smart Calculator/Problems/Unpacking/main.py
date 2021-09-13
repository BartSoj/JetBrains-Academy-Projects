def unpack(input_tuple):
    unpacked = []
    for e in input_tuple:
        if type(e) == tuple:
            for e2 in e:
                unpacked.append(e2)
        else:
            unpacked.append(e)
    return tuple(unpacked)
