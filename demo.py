# simple command line UI for axelrod
print("Importing axelrod...")
import axelrod as axl
print("Done.")
print()
# show a list for users to choose from
print("Choose from the following strategies, enter `-1` when done:")
players = [axl.TitForTat(), axl.Defector(), axl.customPlayer1(), axl.Cooperator(), axl.Grudger()]
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

# print list of result viewing options
resultOptions = ["Wins", "Scores", "Ranking"]
print("Tournament complete. Which results would you like to view?")
i = 0
for i, option in enumerate(resultOptions):
    print("{0}: {1}".format(i, option))
print("-1: Exit")
print()

# prompt user for input
#i = 0
#option = int(input())
#while option != -1:
    


# print the results
print("Results:")
print(results.ranked_names)

