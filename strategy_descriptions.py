# Edit or make a copy of this file depending on what strategies are chosen.

# Serves as the "main menu" for the strategy descriptions
def get_strategy_choice():
    user_exit = False
    while user_exit == False:  
        user_choice = input('''Which strategy would you like to learn about?
        1 - TitforTat
        2 - Defector
        3 - Cooperator
        4 - Grudger
        5 - GoByMajority
        6 - GradualKiller
        7 - Handshake
        8 - WorseAndWorse
        9 - Forgiver
        10 - Adaptive
        0 - Exit back to strategy selection

        ''')
        try:
            selection = int(user_choice)
        except ValueError:
            print("Error. Non-integer detected. Please try again")
            continue

        # User's choice is not in selection
        if selection < 0 or selection > 10:
            print("Please pick a number currently in the given options.")
            continue
        # User wants to return to choosing strategies
        elif selection == 0:
            print("Returning to strategy selection...")
            user_exit = True
            break
        # User selected a strategy
        else:
            provide_description(selection)
            input("Press enter to continue...")

def provide_description(strategy_number):
    if strategy_number == 1:
        print('''Tit for Tat is a strategy that begins by cooperating (C)
        with the opponent. Tit for Tat will continue to cooperate (C) with
        the opponent until the opponent chooses to defect (D). If the opponent
        defects (D), this strategy will attempt to punish the opponent by 
        defecting (D) during the next turn. 
        ''')
    if strategy_number == 2:
        print('''Defector is a strategy that will always defect (D) against
        its opponent, regardless of the opponent's reaction and actions.
        ''')
    if strategy_number == 3:
        print('''Cooperator is a strategy that will always cooperate (C) with
        its opponent, regardless of the opponent's reaction and actions.
        ''')
    if strategy_number == 4:
        print('''Grudger is a strategy that begins by cooperating (C) with
        the opponent. Grudger will continue to cooperate (C) with the opponent
        until the opponent chooses to defect (D). If the opponent defects (D),
        this strategy will attempt to punish the opponent by defecting (D) for
        the remaining turns of the match.
        ''')
    if strategy_number == 5:
        print('''Go By Majority is a strategy that begins by cooperating (C) with
        the opponent. Go By Majority records whether the opponent cooperates (C) or
        chooses to defect (D), with a memory of 40 turns. If the opponent had cooperated
        (C) more times than they have defected (D) during those 40 turns, Go By Majority
        will continue to cooperate (C) with the opponent. If the opponent defected (D)
        more times than cooperated (C), then Go By Majority will continue to defect (D)
        against its opponent. In the case that the opponent has cooperated (C) and
        defected (D) an equal amount of times during the 40 turns of memory, Go By 
        Majority will continue to cooperate (C) with the opponent.
        ''')
    if strategy_number == 6:
        print('''Gradual Killer is a strategy that begins by defecting (D) against
        the opponent for the first 5 turns of the match, and then cooperates (C)
        with the opponent for the 6th and 7th turn of the match. If the opponent
        defects (D) on both turns 6 and 7, Graudal Killer will defect (D) against the 
        opponent the rest of the match. If the opponent only defected (D) once or less 
        during turns 6 and 7, Gradual Killer will cooperate (C) for the rest of the match.
        ''')
    if strategy_number == 7:
        print('''Handshake is a strategy that begins by cooperating (C) on the first
        turn, and defecting (D) on the second turn. If the opponent performed the same
        way during the first two turns, Handshake will cooperate (C) with the opponent
        the rest of the match. If the opponent acted the differently from Handshake
        during the first two turns of the match, Handshake will defect (D) for the rest
        of the match.
        ''')
    if strategy_number == 8:
        print('''Worse and Worse is a strategy that has a chance of defecting (D) equal
        to (current_turn / 1000), meaning that Worse and Worse is more likely to
        defect the longer a match goes on. Otherwise, Worse and Worse cooperates (C)
        with the opponent.
        ''')
    if strategy_number == 9:
        print('''Forgiver is a strategy that begins by cooperating (C) with the opponent.
        If the percentage of turns that the opponent has chosen to defect (D) is greater
        10 percent, Forgiver will defect (D) against the opponent. Otherwise, Forgiver
        will cooperate (C) with the opponent.
        ''')
    if strategy_number == 10:
        print('''Adaptive is a strategy that begins by cooperating (C) with the
        opponent for the first 6 turns, and then defects (D) against the opponent
        for the next 5 turns. From there, Adaptive will cooperate (C) with or defect 
        (D) against the opponent based on what move had scored them more points, and
        recalculates this each turn.
        ''')