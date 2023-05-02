# simple command line UI for axelrod
print("Importing axelrod...")
import axelrod as axl
import random
print("Done.")
print()

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
while (True):
    print("Choose from a 1v1 match to a tournament of 2+ participants: ")
    print("1: Match")
    print("2: Tournament")
    gamemode = int(input())
    if (gamemode > 2 or gamemode < 1):
        print("Please pick 1 or 2")
    else:
        break

# show a list for users to choose from
if gamemode == 2:
    print("Choose from the following strategies, enter `-1` when done:")
else:
    print("Choose from the following strategies:")
players = [axl.TitForTat(), axl.Defector(), axl.Cooperator(), axl.Grudger()] # The () are required for tournament.
playerClasses = [axl.TitForTat, axl.Defector, axl.Cooperator, axl.Grudger] # For transformer use.
i = 0
for i, strategy in enumerate(players):
    print("{0}: {1}".format(i, strategy.name))
if gamemode == 2:
    # add an all option:
    print("{0}: Add one of each".format(i+1))
    print()

# ask user for strategy choices
strategies = []
strategyTransformerGroup = []
i = 0
strategy = int(input("Player {0} strategy: ".format(i)))
while strategy != -1:
    if strategy >= 0 and strategy < len(players):
        strategies.append(players[strategy])
        strategyTransformerGroup.append(playerClasses[strategy])
        i += 1
    elif strategy == len(players):
        for i in range(len(players)):
            strategies.append(players[i])
            strategyTransformerGroup.append(playerClasses[i])
            i+=1
    else:
        print("Invalid strategy.")

    if ((gamemode == 1) and (len(strategies) > 1)):
        break
    strategy = int(input("Player {0} strategy: ".format(i)))


# ask user for number of rounds. Limited to 100 for testing
tooManyRounds = True
print("How many turns should be played between two players? Enter a number: ")
while (tooManyRounds):
    numberOfRounds = int(input())
    if numberOfRounds <= 100:
        break
    print("Too many rounds. Pick a number less than 100: ")

# ask user for amount of noise
print("Noise represents the probability that a player's move will be flipped between C and D")
userNoise = float(input("Input number for amount of noise (0 for no noise, 1 for 100% noise): "))
if userNoise > 1:
    userNoise = 1
    print("Noise set to the maximum of 1")
elif userNoise <= 0:
    userNoise = 0
    print("No noise will be added")

# probabalistic ending of matches
print("Probablistic ending is the probability that a match will end after each move")
probEnd = float(input("Input number for odds of probablistic ending (maximum of 0.5 for 50%): "))
if probEnd > 0.5:
    probEnd = 0.5
    print("Probablistic end chance set to the maximum of 0.5")
elif probEnd <= 0:
    probEnd = 0
    print("No chance for probablistic ending")

# provide an opportunity to transform a strategy. Still flushing out.
chanceToTransform = int(input("Would you like to transform a strategy? \'-1\' to skip, \'1\' to transform: "))
while (chanceToTransform == 1):
    transformations = ["Flip Moves", "Deadlock Breaker", "Apologetic"]
    if (userNoise == 0):
        transformations.append("Noisy")
    for i, strategy in enumerate(strategies):
        print("{0}: {1}".format(i, strategy.name))
    toTransform = int(input("Select a strategy number to transform: "))
    while (toTransform > (len(strategies) - 1) or toTransform > (len(strategyTransformerGroup))):
        # print("Length Strategies: ", len(strategies), " Length Transformables: ", len(strategyTransformerGroup))
        toTransform = int(input("Please select an untransformed strategy that is listed: "))
    stratToTransform = strategies[toTransform]
    for i, transformation in enumerate(transformations):
        print("{0}: {1}".format(i, transformations[i]))
    transformationType = int(input("Select a transformation number: "))
    if transformationType == 0:
        from axelrod.strategy_transformers import FlipTransformer
        strategies.pop(toTransform)
        newStrategy = FlipTransformer()(strategyTransformerGroup[toTransform])
        strategyTransformerGroup.pop(toTransform)
        strategies.append(newStrategy())
        print("Flip transformation applied.")
    elif transformationType == 1:
        from axelrod.strategy_transformers import DeadlockBreakingTransformer
        strategies.pop(toTransform)
        newStrategy = DeadlockBreakingTransformer()(strategyTransformerGroup[toTransform])
        strategyTransformerGroup.pop(toTransform)
        strategies.append(newStrategy())
        print("Deadlock Breaking transformation applied.")
    elif transformationType == 2:
        from axelrod.strategy_transformers import ApologyTransformer
        strategies.pop(toTransform)
        newStrategy = ApologyTransformer()(strategyTransformerGroup[toTransform])
        strategyTransformerGroup.pop(toTransform)
        strategies.append(newStrategy())
        print("Apology transformation applied.")
    elif (transformationType == 3) and (userNoise == 0):
        noiseToAdd = int(input("Enter the desired amount of noise as a percentage (0-100): "))
        while (noiseToAdd < 1):
            print("Minimum of 1% noise required")
            noiseToAdd = int(input("Enter the desired amount of noise as a percentage (0-100): "))
        if (noiseToAdd > 100):
            print("Noise set to the maximum of 100. This is now effectively a flip transformation.")
        numNoise = noiseToAdd / 100.0
        from axelrod.strategy_transformers import NoisyTransformer
        strategies.pop(toTransform)
        newStrategy = NoisyTransformer(numNoise)(strategyTransformerGroup[toTransform])
        strategyTransformerGroup.pop(toTransform)
        strategies.append(newStrategy())
        print("Noisy transformation applied.")
    if (len(strategyTransformerGroup) < 0):
        print("Every strategy has been transformed! Transformations completed")
        break
    chanceToTransform = int(input("Would you like to transform another strategy? \'-1\' to skip, \'1\' to transform: "))
    if (chanceToTransform == -1):
        print("Transformations completed")
else:
    print("Transformations skipped")
    
# create a match or tournament
randomizedRounds = random.randint(5, 15) # randomized number of extra rounds (5-15 for testing)
numberOfRounds += randomizedRounds
if gamemode == 2:
    tournament = axl.Tournament(strategies, turns=numberOfRounds, noise=userNoise, prob_end=probEnd)
else:
    tournament = axl.Match(strategies, turns=numberOfRounds, noise=userNoise, prob_end=probEnd)

# run the tournament
if gamemode == 2: 
    print("Starting tournament...")
# or run the match
else:
    print("Starting match...")
results = tournament.play()

# print the results
if gamemode == 2:
    print("Results listed from most points (left) to least (right):")
    print(results.ranked_names)
else:
    results = tournament.final_score()
    print("Final Scores: " + str(strategies[0]) + " with " + str(results[0]) + " to " + str(strategies[1]) + " with " + str(results[1]))
