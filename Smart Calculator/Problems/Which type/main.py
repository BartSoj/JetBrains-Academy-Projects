import pickle


def retrieve_datatype(path):
    with open(path, "rb") as file:
        data = pickle.load(file)
        return type(data)
