import axelrod as axl
from src.custom_strats import *
from src.functions import *
import random

def basic_selection(gamemode):
    # show a list for users to choose from
    if gamemode == 2:
        print("Choose from the following strategies, enter `-1` when done:")
    else:
        print("Choose from the following strategies:")
    players = [axl.TitForTat(), axl.Defector(), axl.Cooperator(), axl.Grudger()]
    playerClasses = [axl.TitForTat, axl.Defector, axl.Cooperator, axl.Grudger]
    i = 0
    for i, strategy in enumerate(players):
        print("{0}: {1}".format(i, strategy.name))
    if gamemode == 2:
        # add an all option:
        print("{0}: Add one of each".format(i+1))
        print()

    # ask user for strategy choices
    strategies = []
    strategiesTransformerGroup = []
    i = 0
    strategy = int(input("Player {0} strategy: ".format(i)))
    while strategy != -1:
        if strategy >= 0 and strategy < len(players):
            strategies.append(players[strategy])
            strategiesTransformerGroup.append(playerClasses[strategy])
            i += 1
        elif strategy == len(players):
            for i in range(len(players)):
                strategies.append(players[i])
                strategiesTransformerGroup.append(playerClasses[i])
                i+=1
        else:
            print("Invalid strategy.")

        if ((gamemode == 1) and (len(strategies) > 1)):
            break
        strategy = int(input("Player {0} strategy: ".format(i)))
    
    return strategies, strategiesTransformerGroup

def advanced_selection(gamemode):
    # show a list for users to choose from
    if gamemode == 2:
        print("Choose from the following strategies, enter `-1` when done:")
    else:
        print("Choose from the following strategies:")
    adv_players = [axl.TitForTat(), axl.Defector(), axl.Cooperator(), axl.Grudger(),
                   axl.GoByMajority(), axl.GradualKiller(), axl.Handshake(), 
                   axl.WorseAndWorse(), axl.Forgiver(), axl.Adaptive(),
                   axl.Alternator(), axl.Appeaser(), axl.AverageCopier(),
                   axl.BackStabber(), axl.BetterAndBetter(), axl.Doubler(),
                   axl.Negation(), axl.ShortMem(), chaotic_clairvoyant()]
                #    fibTitForTat()]
    adv_playerClasses = [axl.TitForTat, axl.Defector, axl.Cooperator, axl.Grudger,
                   axl.GoByMajority, axl.GradualKiller, axl.Handshake, 
                   axl.WorseAndWorse, axl.Forgiver, axl.Adaptive,
                   axl.Alternator, axl.Appeaser, axl.AverageCopier,
                   axl.BackStabber, axl.BetterAndBetter, axl.Doubler,
                   axl.Negation, axl.ShortMem, chaotic_clairvoyant]
                #    fibTitForTat] This strat takes too long to run
    i = 0
    for i, strategy in enumerate(adv_players):
        print("{0}: {1}".format(i, strategy.name))
    if gamemode == 2:
        # add an all option:
        print("{0}: Add one of each".format(i+1))
        print("{0}: Add a random selection of strategies".format(i+2))
        print()

    # ask user for strategy choices
    adv_strategies = []
    adv_strategiesTransformerGroup = []
    i = 0
    strategy = int(input("Player {0} strategy: ".format(i)))
    while strategy != -1:
        if strategy >= 0 and strategy < len(adv_players):
            adv_strategies.append(adv_players[strategy])
            adv_strategiesTransformerGroup.append(adv_playerClasses[strategy])
            i += 1
        elif strategy == len(adv_players):
            for i in range(len(adv_players)):
                adv_strategies.append(adv_players[i])
                adv_strategiesTransformerGroup.append(adv_playerClasses[i])
                i+=1
        elif strategy == len(adv_players) + 1:
            print("Would you like to allow duplicates? (y/n): ")
            allowDuplicates = getInput(data_type=str)
            allowDuplicates = allowDuplicates.lower()
            # ensure valid input
            while allowDuplicates != "y" and allowDuplicates != "n":
                print("Invalid input.")
                allowDuplicates = getInput("Allow duplicates? (y/n): ",data_type=str)
                allowDuplicates = allowDuplicates.lower()
            
            
            if allowDuplicates == "y":
                numPlayers = getInput("How many players would you like to add?: ", data_type=int)
                # ensure valid input
                while numPlayers < 0:
                    print("Invalid number of players.")
                    numPlayers = getInput("Select number of players: ",data_type=int)
                    
                for i in range(numPlayers):
                    playerNum = random.randint(0,len(adv_players)-1)
                    adv_strategies.append(adv_players[playerNum])
                    adv_strategiesTransformerGroup.append(adv_playerClasses[playerNum])
            else:
                numPlayers = getInput(f"How many players would you like to add? (1-{len(adv_players)}): ", data_type=int)
                # ensure valid input
                while numPlayers < 1 or numPlayers > len(adv_players):
                    print("Invalid number of players.")
                    numPlayers = getInput("Select number of players: ",data_type=int)
                    
                selectionList = adv_players.copy()
                random.shuffle(selectionList)
                for i in range(numPlayers):
                    adv_strategies.append(selectionList[i])
                    adv_strategiesTransformerGroup.append(adv_playerClasses[i])
        else:
            print("Invalid strategy.")

        if ((gamemode == 1) and (len(adv_strategies) > 1)):
            break
        strategy = int(input("Player {0} strategy: ".format(i)))
    
    return adv_strategies, adv_strategiesTransformerGroup