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

from axelrod import result_set, tournament as tourney
def resultsToDF(results, tournament):

    # Make sure results is <class 'axelrod.result_set.ResultSet'>
    # make sure tournament is <class 'axelrod.tournament.Tournament'>
    if not isinstance(results, result_set.ResultSet):
        raise TypeError("results must be a ResultSet")
    if not isinstance(tournament, tourney.Tournament):
        raise TypeError("tournament must be a Tournament")
    

    df = pd.DataFrame(results.summarise())
    df = df.iloc[:, 0:5]

    # additional info
    extraData = {
        'Total score': [sum(score) for score in results.scores],
        'Avg. score per turn': [round(sum(score) / (len(score) * tournament.turns), 2) for score in results.scores],
        'Score Std. deviation': [round(pd.Series(score).std(), 2) for score in results.scores],
        'Normalised Score': [round(sum(score) / (len(score) * tournament.turns * len(results.players)), 2) for score in results.scores]
    }

    # append columns to df
    for key in extraData:
        df[key] = extraData[key]

    return df