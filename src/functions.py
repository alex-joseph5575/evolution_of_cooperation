# import axelrod as axl
from axelrod import result_set, tournament as tourney
import matplotlib.pyplot as plt
import random
import os
from os import path
import sys
import pandas as pd


def outputToCsv(df, filename="results"):
    """
    Saves a Pandas DataFrame to a CSV file in the outputs/ directory.
    If a file with the same name already exists, increments the filename to avoid overwriting.
    :param df: Pandas DataFrame to save
    :param filename: Name of the output file (without the .csv extension)
    :return: None
    """
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


def resultsToDF(results, tournament):
    """
    Converts a ResultSet object from Axelrod to a Pandas DataFrame.
    Adds additional columns for useful statistics such as total score and normalized score.
    :param results: ResultSet object from Axelrod
    :param tournament: Tournament object from Axelrod
    :return: Pandas DataFrame containing the results of the tournament
    """
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


def PrintMatchResults(results, title="Match Results", player1="Player 1", player2="Player 2"):
    """
    Generates a formatted table of iterated prisoner's dilemma match results.

    Parameters:
    results (List[tuple[str,str]) (from axl.Match(_).play()): The list of tuples representing the moves made by two players in the match.
    title (str): The title of the table. Defaults to "Match Results".
    player1 (str): The name of the first player. Defaults to "Player 1".
    player2 (str): The name of the second player. Defaults to "Player 2".

    Returns:
    None: This function does not return a value, but instead outputs the table to the console.
    """
    if not isinstance(player1, str):
        raise TypeError("player1 must be a string")
    if not isinstance(player2, str):
        raise TypeError("player2 must be a string")

    turn_header = "Turn".center(len(str(len(results)))+2)
    p1_header = player1.center(len(player1)+2)
    p2_header = player2.center(len(player2)+2)

    print(title + ":")
    print("-"*(len(title)+len(p1_header)+len(p2_header)+4))
    print(f"|  {turn_header} |  {p1_header} |  {p2_header} |")
    print("-"*(len(title)+len(p1_header)+len(p2_header)+4))
    for i, (p1_move, p2_move) in enumerate(results):
        p1_move_str = str(p1_move).center(len(player1)+2)
        p2_move_str = str(p2_move).center(len(player2)+2)
        turn_str = str(i+1).center(len(turn_header))
        print(f"|  {turn_str} |  {p1_move_str} |  {p2_move_str} |")
    print("-"*(len(title)+len(p1_header)+len(p2_header)+4))


def PlotMatchResults(results, title="Match Results", player1="Player 1", player2="Player 2"):
    """
    Plots the cumulative scores of two players over a series of turns in an iterated prisoner's dilemma match.

    Parameters:
    results (List[Tuple[int, int]]) (from axl.Match(_).scores()): A list of tuples representing the scores of each turn of the match.
    title (str): A string representing the title of the plot. Default is "Match Results".
    player1 (str): A string representing the name of the first player. Default is "Player 1".
    player2 (str): A string representing the name of the second player. Default is "Player 2".

    Returns:
    None: This function does not return anything, it simply displays the plot.
    """
    if not isinstance(player1, str):
        raise TypeError("player1 must be a string")
    if not isinstance(player2, str):
        raise TypeError("player2 must be a string")

    p1_scores = [0]
    p2_scores = [0]

    for i, (p1_move, p2_move) in enumerate(results):
        if p1_move > p2_move:
            p1_scores.append(p1_scores[-1] + 3)
            p2_scores.append(p2_scores[-1] + 0)
        elif p1_move < p2_move:
            p1_scores.append(p1_scores[-1] + 0)
            p2_scores.append(p2_scores[-1] + 3)
        else:
            p1_scores.append(p1_scores[-1] + 1)
            p2_scores.append(p2_scores[-1] + 1)

    turns = range(len(results) + 1)

    plt.plot(turns, p1_scores, label=player1)
    plt.plot(turns, p2_scores, label=player2)
    plt.title(title)
    plt.xlabel("Turn")
    plt.ylabel("Score")
    plt.xticks(turns)
    plt.legend()
    plt.show()
