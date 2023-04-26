import axelrod as axl
from custom_strats import *
import random

def basic_selection(gamemode):
    # show a list for users to choose from
    if gamemode == 2:
        print("Choose from the following strategies, enter `-1` when done:")
    else:
        print("Choose from the following strategies:")
    players = [axl.TitForTat(), axl.Defector(), axl.Cooperator(), axl.Grudger()]
    i = 0
    for i, strategy in enumerate(players):
        print("{0}: {1}".format(i, strategy.name))
    if gamemode == 2:
        # add an all option:
        print("{0}: Add one of each".format(i+1))
        print()

    # ask user for strategy choices
    strategies = []
    i = 0
    strategy = int(input("Player {0} strategy: ".format(i)))
    while strategy != -1:
        if strategy >= 0 and strategy < len(players):
            strategies.append(players[strategy])
            i += 1
        elif strategy == len(players):
            for i in range(len(players)):
                strategies.append(players[i])
                i+=1
        else:
            print("Invalid strategy.")

        if ((gamemode == 1) and (len(strategies) > 1)):
            break
        strategy = int(input("Player {0} strategy: ".format(i)))
    
    return strategies

def advanced_selection(gamemode):
    # show a list for users to choose from
    if gamemode == 2:
        print("Choose from the following strategies, enter `-1` when done:")
    else:
        print("Choose from the following strategies:")
    adv_players = [axl.TitForTat(), axl.Defector(), axl.Cooperator(), axl.Grudger()]
    i = 0
    for i, strategy in enumerate(adv_players):
        print("{0}: {1}".format(i, strategy.name))
    if gamemode == 2:
        # add an all option:
        print("{0}: Add one of each".format(i+1))
        print()

    # ask user for strategy choices
    adv_strategies = []
    i = 0
    strategy = int(input("Player {0} strategy: ".format(i)))
    while strategy != -1:
        if strategy >= 0 and strategy < len(adv_players):
            adv_strategies.append(adv_players[strategy])
            i += 1
        elif strategy == len(adv_players):
            for i in range(len(adv_players)):
                adv_strategies.append(adv_players[i])
                i+=1
        else:
            print("Invalid strategy.")

        if ((gamemode == 1) and (len(adv_strategies) > 1)):
            break
        strategy = int(input("Player {0} strategy: ".format(i)))
    
    return adv_strategies