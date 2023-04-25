# import axelrod as axl
import random
import os
from os import path
import sys
import pandas as pd


def outputToCsv(df, filename="results"):
    # Check if the input is a Pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a Pandas DataFrame")
    
    # if filename ends in .csv, remove it
    if filename[-4:] == ".csv":
        filename = filename[:-4]

    # check if file exists
    if (path.exists("outputs/" + filename + ".csv")):
        
        # increment filename
        i = 1
        while (path.exists("outputs/" + filename + "_{0}.csv".format(i))):
            i += 1
        
        df.to_csv("outputs/" + filename + "_{0}.csv".format(i), index=False)
        print("File saved as " + filename + "_{0}.csv".format(i))
    
    else:
        df.to_csv("outputs/" + filename + ".csv", index=False)
        print("File saved as " + filename + ".csv")

