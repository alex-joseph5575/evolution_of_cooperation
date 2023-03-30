# git clone https://github.com/Austin-Simpson/Axelrod
import sys
sys.path.append('../Axelrod/')

# Now you can import modules or packages from the specified folder
print("Importing axelrod...")
import axelrod_evo as axl


print("Done.")
print()
# show a list for users to choose from
print("Choose from the following strategies, enter `-1` when done:")
players = [axl.TitForTat(), axl.fibTitForTat(),  axl.Defector(), axl.Cooperator(), axl.Grudger()]
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
print("Results:")
print(results.ranked_names)

