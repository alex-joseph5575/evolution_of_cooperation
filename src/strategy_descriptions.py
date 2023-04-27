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
        11 - Alternator
        12 - Appeaser
        13 - AverageCopier
        14 - Backstabber
        15 - BetterAndBetter
        16 - Doubler
        17 - Negation
        18 - ShortMem
        19 - chaotic_clairvoyant
        20 - fibTitForTat
        0 - Exit back to strategy selection

        ''')
        try:
            selection = int(user_choice)
        except ValueError:
            print("Error. Non-integer detected. Please try again")
            continue

        # User's choice is not in selection
        if selection < 0 or selection > 20:
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
        chooses to defect (D). If the opponent had cooperated (C) more times than 
        they have defected (D) in Go By Majority's memory, Go By Majority
        will continue to cooperate (C) with the opponent. If the opponent defected (D)
        more times than cooperated (C), then Go By Majority will continue to defect (D)
        against its opponent. In the case that the opponent has cooperated (C) and
        defected (D) an equal amount of times according to Go By Majority's memory, 
        Go By Majority will continue to cooperate (C) with the opponent.
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
    if strategy_number == 11:
        print('''Alternator is a strategy that begins by cooperating (C) with the
        opponent. From there, Alterator will defect (D) if its previous turn was
        spent cooperating (C) with the opponent, and will cooperate (C) if its 
        previous turn was spent defecting (D) against the opponent.
        ''')
    if strategy_number == 12:
        print('''Appeaser is a strategy that begins by cooperating (C) with the
        opponent. From there, if the opponent has defected (D) against Appeaser
        during the previous round, Appeaser will defect (D) if it cooperated
        (C) during the previous round OR Appeaser will cooperate (C) if it 
        defected (D) during the previous round. If the opponent continues to 
        cooperate (C) with Appeaser, Appeaser will continue to cooperate (C).
        ''')
    if strategy_number == 13:
        print('''Average Copier is a strategy that begins by a 50/50 chance of either
        cooperating (C) with or defecting (D) against the opponent. From there, Average
        Copier's probability of cooperating (C) with the opponent is determined by:
        # of opponent Cooperations / # opponent's total moves.
        ''')
    if strategy_number == 14:
        print('''Backstabber is a strategy that begins by cooperating (C) with the
        opponent. From there, Backstabber will continue to cooperate (C) with the
        opponent until the opponent has defected (D) 4 times. Backstabber will then
        always defect (D) against the opponent for the rest of the match. Regardless
        of whether the opponent has defected (D) 4 times during the match or not, Backstabber
        will always defect (D) against the opponent during the last 2 rounds of the match.
        ''')
    if strategy_number == 15:
        print('''Better and Better is a strategy that has a chance of defecting (D)
        against the opponent each turn determined by: (1000 - current turn) / 1000. 
        This means that as the match continues on, Better and Better has a better
        chance of cooperating (C) with the opponent.
        ''')
    if strategy_number == 16:
        print('''Doubler is a strategy that will cooperate (C) with the opponent unless
        the opponent has defected (D) during the previous round and the number of times
        that the opponent has cooperated (C) is less than or equal to 2 times the number 
        of times the opponent has defected (D). If both conditions are met, Doubler
        will defect (D) against the opponent.
        ''')
    if strategy_number == 17:
        print('''Negation is a strategy that begins by a 50/50 chance of either
        cooperating (C) with or defecting (D) against the opponent. From there, Negation
        will defect (D) if the opponent had cooperated (C) during the previous turn, and
        cooperate (C) if the opponent had defected (D) during the previous turn.
        ''')
    if strategy_number == 18:
        print('''ShortMem is a strategy that begins by cooperating (C) with the opponent
        for the first 10 turns, recording the oppnent's actions during those turns. After 
        the 10th turn, if the opponent had cooperated (C) 30% more times than defecting (D) 
        during the first 10 turns, ShortMem will continue to cooperate (C) for the rest of
        the match. If the opponent had defected (D) 30% more times than cooperating (C) 
        during the first 10 turns, ShortMem will proceed by defecting (D) the rest of the 
        match. If niether condition is met, ShortMem will utilize the strategy of Tit For Tat,
        that is, cooperate (C) with the opponent unless the opponent has defected (D) during
        the previous turn. If the opponent defected (D) during the previous turn, defect (D)
        this turn as punishment.
        ''')
    if strategy_number == 19:
        print('''Chaotic Clairvoyant is a strategy that begins by defecting (D) against the
        opponent. From there, Chaotic Clairvoyant looks at the opponent's Last 3 moves (or 
        however many moves the opponent has made if there has been less than 3 turns during 
        the match), and does the opposite of that opponent's most frequently performed move.
        In other words, if the opponent had cooperated (C) at least 2 times during the last 
        two turns (or more than defected (D) if < 3 turns), Chaotic Clairvoyant will defect (D)
        the current turn, and if the opponent had defected (D) at least 2 times during the last
        two turns (or more than cooperated (C) if < 3 turns), Chaotic Clairvoyant will cooperate
        (C) the current turn. In the case that the opponent had cooperated (C) and defected (D)
        an equal amount of times due to still being under 3 turns, Chaotic Clairvoyant will
        defect (D) by default.
        ''')
    if strategy_number == 20:
        print('''Fib Tit for Tat is a strategy that cooperates (C) with the opponent during
        the first turn of the match. From there, Fib Tit for Tat will copy its opponent's
        previous move during the match, but has a chance of defecting (D) outright based on the
        current turn count of the match. This chance of defecting (D) outright is 
        a one-in-fib(turn count) chance, where fib(turn count) is equal to the number in the 
        Fibonacci sequence associated with the current turn number. This means that as the match
        goes on, the chances of Fib Tit for Tat defecting (D) regardless of the opponent's last
        move decreases the longer the match goes on.
        ''')