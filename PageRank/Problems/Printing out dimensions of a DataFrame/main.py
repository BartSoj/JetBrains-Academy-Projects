import pandas as pd


def print_dim(df):
    print("This DataFrame contains {} rows and {} columns".format(*df.shape))
