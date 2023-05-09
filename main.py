print("importing...")
from src.custom_strats import *
from src.misc_functions import *
from src.strategy_descriptions import *
from src.functions import *
import random
from src.strategy_selection import *
import axelrod as axl
print("Done.")
print()

advanced = 0
isPlaying = 1

# Provides some background info for users
print('''
The Prisoners' Dilemma is a hypothetical scenario in which two players are given a choice to
without knowing the other individual's decision until both have chosen. The options are to
either Cooperate with the other individual for mutual benefit, or to Defect and receive a
larger benefit that only the Defector would receive if the other individual decided to
Cooperate. If both players Defect, then the benefit that both players receive would be less
than the mutual benefit from both players Cooperating.

For this simulation, points are rewarded for different interactions as follows:
- Cooperate (C) and Cooperate (C): Both players are awarded 3 points
- Defect (D) and Cooperate (C): Defector is awarded 5 points and Cooperator is awarded 0 points
- Defect (D) and Defect (D): Both players are awarded 1 point
''')
# have user select between a match or a tournament
while isPlaying == 1:
    while (True):
        selection = -1
        if advanced == 0:
            print("Advanced mode is currently off. Only a basic selection of strategies will be able to be selected.\n")
        else:
            print(
                "Advanced mode is currently on. A larger selection of strategies will be able to be selected.\n")
        print("Choose from a 1v1 match to a tournament of 2+ participants: ")
        print("1: Match")
        print("2: Tournament")
        print("3: Toggle Advanced Mode")
        print("0: Read description of strategies")
        selection = getInput(data_type=int)

        # Error handling for non-integers
        try:
            gamemode = int(selection)
        except ValueError:
            print("Error. Non-integer input detected. Please try again.")
            continue

        # User wanted to read up on strategies
        if gamemode == 0:
            get_strategy_choice()
            continue
        # User wanted to turn on or turn off advanced mode
        if gamemode == 3:
            if advanced == 0:
                print("Advanced mode toggled: ON\n")
                advanced = 1
                continue
            else:
                print("Advanced mode toggled: OFF\n")
                advanced = 0
                continue
        # User provided a non-option
        elif (gamemode > 2 or gamemode < 1):
            print("Please pick 1 or 2")
        else:
            break

    if advanced == 0:
        strategies, strategyTransformerGroup = basic_selection(gamemode)
    else:
        strategies, strategyTransformerGroup = advanced_selection(gamemode)

    # ask user for number of rounds. Limited to 100 for testing
    tooManyRounds = True
    print("How many turns should be played between two players? Enter a number: ")
    while (tooManyRounds):
        numberOfRounds = int(getInput(data_type=int))
        if numberOfRounds <= 100:
            break
        print("Too many rounds. Pick a number less than 100: ")

    # ask user for amount of noise
    print("Noise represents the probability that a player's move will be flipped between C and D")
    userNoise = float(
        getInput("Input number for amount of noise (0 for no noise, 1 for 100% noise): ", data_type=float))
    if userNoise > 1:
        userNoise = 1
        print("Noise set to the maximum of 1")
    elif userNoise <= 0:
        userNoise = 0
        print("No noise will be added")

    # probabalistic ending of matches
    print("Probablistic ending is the probability that a match will end after each move")
    probEnd = float(
        getInput("Input number for odds of probablistic ending (maximum of 0.5 for 50%): ", data_type=float))
    if probEnd > 0.5:
        probEnd = 0.5
        print("Probablistic end chance set to the maximum of 0.5")
    elif probEnd <= 0:
        probEnd = 0
        print("No chance for probablistic ending")

    # provide an opportunity to transform a strategy
    chanceToTransform = int(getInput("Would you like to transform a strategy? \'-1\' to skip, \'1\' to transform: ", data_type=int))
    while (chanceToTransform == 1):
        transformations = ["Flip Moves",
                           "Deadlock Breaker", "Retaliate Until Apology"]
        # only allow for noisy transformation if tournament does not have noise
        if (userNoise == 0):
            transformations.append("Noisy")
        for i, strategy in enumerate(strategies):
            print("{0}: {1}".format(i, strategy.name))
        toTransform = int(getInput("Select a strategy number to transform: ", data_type=int))
        while (toTransform > (len(strategies) - 1) or toTransform > (len(strategyTransformerGroup))):
            # print("Length Strategies: ", len(strategies), " Length Transformables: ", len(strategyTransformerGroup))
            toTransform = int(
                getInput("Please select an untransformed strategy that is listed: ", data_type=int))
        stratToTransform = strategies[toTransform]
        for i, transformation in enumerate(transformations):
            print("{0}: {1}".format(i, transformations[i]))
        transformationType = int(getInput("Select a transformation number: ", data_type=int))
        if transformationType == 0:
            from axelrod.strategy_transformers import FlipTransformer
            strategies.pop(toTransform)
            newStrategy = FlipTransformer()(
                strategyTransformerGroup[toTransform])
            strategyTransformerGroup.pop(toTransform)
            strategies.append(newStrategy())
            print("Flip transformation applied.")
        elif transformationType == 1:
            from axelrod.strategy_transformers import DeadlockBreakingTransformer
            strategies.pop(toTransform)
            newStrategy = DeadlockBreakingTransformer()(
                strategyTransformerGroup[toTransform])
            strategyTransformerGroup.pop(toTransform)
            strategies.append(newStrategy())
            print("Deadlock Breaking transformation applied.")
        elif transformationType == 2:
            from axelrod.strategy_transformers import RetaliateUntilApologyTransformer
            strategies.pop(toTransform)
            newStrategy = RetaliateUntilApologyTransformer()(
                strategyTransformerGroup[toTransform])
            strategyTransformerGroup.pop(toTransform)
            strategies.append(newStrategy())
            print("Retaliate Until Apology transformation applied.")
        elif (transformationType == 3) and (userNoise == 0):
            noiseToAdd = int(
                getInput("Enter the desired amount of noise as a percentage (0-100): ", data_type=int))
            while (noiseToAdd < 1):
                print("Minimum of 1% noise required")
                noiseToAdd = int(
                    getInput("Enter the desired amount of noise as a percentage (0-100): ", data_type=int))
            if (noiseToAdd > 100):
                print(
                    "Noise set to the maximum of 100. This is now effectively a flip transformation.")
            numNoise = noiseToAdd / 100.0
            from axelrod.strategy_transformers import NoisyTransformer
            strategies.pop(toTransform)
            newStrategy = NoisyTransformer(numNoise)(
                strategyTransformerGroup[toTransform])
            strategyTransformerGroup.pop(toTransform)
            strategies.append(newStrategy())
            print("Noisy transformation applied.")
        if ((len(strategyTransformerGroup) - 1) < 0):
            print("Every strategy has been transformed! Transformations completed")
            break
        chanceToTransform = int(getInput("Would you like to transform another strategy? \'-1\' to skip, \'1\' to transform: ", data_type=int))
        if (chanceToTransform == -1):
            print("Transformations completed")
    else:
        print("Transformations skipped")

    # create a match or tournament
    # randomized number of extra rounds (5-15 for testing)
    randomizedRounds = random.randint(5, 15)
    numberOfRounds += randomizedRounds
    if gamemode == 2:
        tournament = axl.Tournament(
            strategies, turns=numberOfRounds, noise=userNoise, prob_end=probEnd)
    else:
        tournament = axl.Match(
            strategies, turns=numberOfRounds, noise=userNoise, prob_end=probEnd)

    # run the tournament
    if gamemode == 2:
        print("Starting tournament...")
    # or run the match
    else:
        print("Starting match...")
    results = tournament.play()

    # print the results
    # TODO: Austin
    if gamemode == 2:
        print("Results listed from most points (left) to least (right):")
        print(results.ranked_names)
        df = resultsToDF(results, tournament)
        selection = -1
        while (selection != 0):
            print("What would you like to do with the results?")
            print("1. Plot tournament results")
            print("2. Plot example match between two strategies")
            print("3. Print the tournament results to the console")
            print("4. Print example match between two strategies to the console")
            print("5. Save the results to a CSV file")
            print("0. Exit")
            selection = getInput(data_type=int)
            if selection == 1:
                plot_bar_chart(df)
            elif selection == 2:
                print("Match between which two strategies?")
                for i, strategy in enumerate(strategies):
                    print("{0}: {1}".format(i, strategy.name))
                strat1 = int(getInput("Select the first strategy: ", data_type=int))
                strat2 = int(getInput("Select the second strategy: ", data_type=int))
                while (strat1 > (len(strategies) - 1) or strat2 > (len(strategies) - 1)):
                    strat1 = int(getInput("Please select a strategy that is listed: ", data_type=int))
                    strat2 = int(getInput("Please select a strategy that is listed: ", data_type=int))
                exampleMatch = axl.Match([strategies[strat1], strategies[strat2]], turns=numberOfRounds, noise=userNoise, prob_end=probEnd)
                exampleMatchResults = exampleMatch.play()
                PlotMatchResults(exampleMatch.scores(), player1=strategies[strat1].name, player2=strategies[strat2].name)
            elif selection == 3:
                print(df)
            elif selection == 4:
                print("Match between which two strategies?")
                for i, strategy in enumerate(strategies):
                    print("{0}: {1}".format(i, strategy.name))
                strat1 = int(getInput("Select the first strategy: ", data_type=int))
                strat2 = int(getInput("Select the second strategy: ", data_type=int))
                while (strat1 > (len(strategies) - 1) or strat2 > (len(strategies) - 1)):
                    strat1 = int(getInput("Please select a strategy that is listed: ", data_type=int))
                    strat2 = int(getInput("Please select a strategy that is listed: ", data_type=int))
                exampleMatch = axl.Match([strategies[strat1], strategies[strat2]], turns=numberOfRounds, noise=userNoise, prob_end=probEnd)
                exampleMatchResults = exampleMatch.play()
                if len(exampleMatchResults) > 10:
                    print(f"Match is {len(exampleMatchResults)} rounds long. Would you like to limit number of rounds displayed?")
                    print("Enter 0 for no limit, or enter a number to limit the number of rounds displayed")
                    limit = getInput(data_type=int)
                PrintMatchResults(exampleMatchResults, player1=strategies[strat1].name, player2=strategies[strat2].name, turn_limit=limit)
            elif selection == 5:
                filename = getInput("Enter the name of the file to save the results to (leave blank for default name): ", data_type=str)
                outputToCsv(df, filename)
                
            elif selection == 0:
                break
            else: 
                print("Invalid input")

    else:
        results = tournament.final_score()
        print("Final Scores: \n=============\n" + str(strategies[0]) + ": " + str(
            results[0]) + " points\n" + str(strategies[1]) + ": " + str(results[1]) + " points")
        PlotMatchResults(
            tournament.scores(), player1=strategies[0].name, player2=strategies[1].name)
        PrintMatchResults(tournament.play(), player1=strategies[0].name, player2=strategies[1].name, turn_limit=20)

    print("Would you like to play another game?")
    print("1. Yes")
    print("2. No")
    while (True):
        option = int(getInput(data_type=int))

        if option == 1:
            break
        elif option == 2:
            isPlaying = 0
            break
        else:
            print("Invalid input")
