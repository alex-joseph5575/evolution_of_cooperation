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
loop = 1

while loop == 1:
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

    flag = 1

    # Basic version
    if flag == 0:
            # print list of result viewing options
        resultOptions = ["Wins", "Scores", "Ranking"]
        print("Tournament complete. Which results would you like to view?")
        i = 0
        for i, option in enumerate(resultOptions):
            print("{0}: {1}".format(i, option))
        print("-1: Exit")
        print()

        # prompt user for input and print results
        i = 0
        option = int(input())
        while option != -1:
            match option:
                case 0:
                    print(results.wins)
                case 1:
                    print(results.scores)
                case 2:
                    print(results.ranked_names)
                case _:
                    print("Invalid input")
            for i, option in enumerate(resultOptions):
                print("{0}: {1}".format(i, option))
            print("-1: Exit")
            i = 0
            option = int(input())

    # Advanced version
    elif flag == 1:
        # print list of result viewing options
        resultOptions = ["Wins", "Scores", "Ranking", "Normalised Scores", "Payoffs", "Initial Cooperation Rates", "Cooperation Counts"]
        print("Tournament complete. Which results would you like to view?")
        i = 0
        for i, option in enumerate(resultOptions):
            print("{0}: {1}".format(i, option))
        print("-1: Exit")
        print()

        # prompt user for input and print results
        i = 0
        option = int(input())
        while option != -1:
            match option:
                case 0:
                    print(results.wins)
                case 1:
                    print(results.scores)
                case 2:
                    print(results.ranked_names)
                case 3:
                    print(results.normalised_scores)
                case 4:
                    print(results.payoff_matrix)
                case 5:
                    print(results.initial_cooperation_rate)
                case 6:
                    print(results.cooperation)
                case _:
                    print("Invalid input")
            for i, option in enumerate(resultOptions):
                print("{0}: {1}".format(i, option))
            print("-1: Exit")
            i = 0
            option = int(input())

        print("Would you like to play another game?")
        print("1. Yes")
        print("2. No")
        while loop == 1:
            option = int(input())

            if option == 1:
                break
            elif option == 2:
                loop = 0
            else:
                print("Invalid input")



        


    # print the results
    #print("Results listed from most points (left) to least (right):")
    #print(results.ranked_names)

    # print the results
    #print("Results:")
    #print(results.ranking)


