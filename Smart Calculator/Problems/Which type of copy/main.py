import copy


def detect_copy():
    obj = [[1, 2], [3, 4]]
    copy_obj = copying_machine(obj)
    if id(copy_obj[0]) == id(obj[0]):
        return "shallow copy"
    else:
        return "deep copy"