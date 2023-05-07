# import axelrod as axl
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

from axelrod import result_set, tournament as tourney
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


import matplotlib.pyplot as plt

def plot_bar_chart(df, title="Bar chart of total scores"):
    """
    Plots a bar chart of the total scores for each strategy in the tournament.
    :param df: Pandas DataFrame containing the results of the tournament
    :param title: Title of the plot (default: "Bar chart of total scores")
    :return: None
    """
    fig, ax = plt.subplots()
    ax.bar(df["Name"], df["Total score"])
    ax.set_xlabel("Strategy")
    ax.set_ylabel("Total score")
    ax.set_title(title)
    plt.show()


def plot_heatmap(df, title="Heatmap of scores for each pair of strategies"):
    """
    Plots a heatmap of the scores for each pair of strategies in the tournament.
    :param df: Pandas DataFrame containing the results of the tournament
    :param title: Title of the plot (default: "Heatmap of scores for each pair of strategies")
    :return: None
    """
    pivot = df.pivot(index="Player 1", columns="Player 2", values="Score")
    fig, ax = plt.subplots()
    im = ax.imshow(pivot, cmap='Blues')
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels(pivot.columns, rotation=90)
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index)
    ax.set_title(title)
    plt.colorbar(im)
    plt.show()


def plot_box_plot(df, title="Box plot of scores for each strategy"):
    """
    Plots a box plot of the scores for each strategy in the tournament.
    :param df: Pandas DataFrame containing the results of the tournament
    :param title: Title of the plot (default: "Box plot of scores for each strategy")
    :return: None
    """
    fig, ax = plt.subplots()
    ax.boxplot(df["Score"], labels=df["Name"])
    ax.set_xlabel("Strategy")
    ax.set_ylabel("Score")
    ax.set_title(title)
    plt.show()

def plot_line_chart(df, player_1=None, player_2=None, title="Line chart of scores over time"):
    """
    Plots a line chart of the scores over time for a single match between two strategies.
    If player_1 and player_2 are not specified, the first two rows in the DataFrame will be used.
    :param df: Pandas DataFrame containing the results of the tournament
    :param player_1: Index of the first row (default: None)
    :param player_2: Index of the second row (default: None)
    :param title: Title of the plot (default: "Line chart of scores over time")
    :return: None
    """
    if player_1 is None or player_2 is None:
        if len(df) < 2:
            raise ValueError("DataFrame does not contain data for at least two players")
        player_1, player_2 = df.index[:2]

    subset = df.loc[[player_1, player_2]]
    fig, ax = plt.subplots()
    ax.plot(subset["Turn"], subset["Score"], label=f"{subset.iloc[0]['Name']} vs {subset.iloc[1]['Name']}")
    ax.set_xlabel("Turn")
    ax.set_ylabel("Score")
    ax.set_title(title)
    ax.legend()
    plt.show()

def plot_all(df, tournament, title_prefix="Tournament Results"):
    """
    Creates all visualizations for the tournament results.
    :param df: Pandas DataFrame containing the results of the tournament
    :param tournament: Tournament object from Axelrod
    :param title_prefix: Prefix to use for all plot titles (default: "Tournament Results")
    :return: None
    """
    # Create bar chart of total scores
    title = title_prefix + " - Bar chart of total scores"
    plot_bar_chart(df, title=title)

    # Create heatmap of scores for each pair of strategies
    title = title_prefix + " - Heatmap of scores for each pair of strategies"
    plot_heatmap(df, title=title)

    # Create box plot of scores for each strategy
    title = title_prefix + " - Box plot of scores for each strategy"
    plot_box_plot(df, title=title)

    # Create line chart of scores over time for a single match
    title = title_prefix + " - Line chart of scores over time"
    if len(df) < 2:
        player_1 = player_2 = None
    else:
        player_1, player_2 = df.index[:2]
    plot_line_chart(df, player_1, player_2, title=title)
