# simple command line UI for axelrod
print("Importing axelrod...")
import axelrod as axl
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
# show a list for users to choose from
print("Choose from the following strategies, enter `-1` when done:")
players = [axl.TitForTat(), axl.Defector(), axl.Cooperator(), axl.Grudger()]
i = 0
for i, strategy in enumerate(players):
    print("{0}: {1}".format(i, strategy.name))

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
    strategy = int(input("Player {0} strategy: ".format(i)))

# create a tournament
tournament = axl.Tournament(strategies)


# run the tournament
print("Starting tournament...")
results = tournament.play()

# print the results
print("Results listed from most points (left) to least (right):")
print(results.ranked_names)

