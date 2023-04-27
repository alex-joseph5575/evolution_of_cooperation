import axelrod as axl

C, D = axl.Action.C, axl.Action.D


class example(axl.Player):
    """
    This is an example strategy to show you the structure of a strategy.
    It cooperates on the first move and then defects if and only if the opponent
    defected on the previous move.
    """

    # These are various properties for the strategy
    name = "example"

    classifier = {
        "memory_depth": 1,  # Four-Vector = (1.,0.,1.,0.)
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def strategy(self, opponent):
        """This is where you define the strategy"""
        # First move
        if not self.history:    # If the length of history is 0, i.e. the first round
            return C            
        
        # The rest of your moves
        if opponent.history[-1] == D:   # If the opponent's last move was D
            return D                    # Defect
        return C                        # Otherwise cooperate.
    

# next strategy
class chaotic_clairvoyant(axl.Player):
    """
    A player looks at the last 3 (or however many were performed if less than 3) actions of their
    opponent and does the opposite of their most frequently performed move.
    First move of the match will be D.
    """

    # These are various properties for the strategy
    name = "chaotic_clairvoyant"
    classifier = {
        "memory_depth": 3,  # Four-Vector = (1.,0.,1.,0.)
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def strategy(self, opponent):
        """This is the actual strategy"""
        c_count = 0
        d_count = 0
        # First move
        if not self.history:
            return D
        # If opponent hasn't played 3 moves yet
        if len(opponent.history) < 3:
            for o_move in opponent.history:
                if o_move == D:
                    d_count += 1
                else:
                    c_count += 1
            if d_count > c_count:
                return C
            return D
        # If opponent has played 3 moves
        else:
            for o_move in opponent.history[-3:]:
                if o_move == D:
                    d_count += 1
                else:
                    c_count += 1
            if d_count > c_count:
                return C
            return D


from misc_functions import (
    fib, getRandom
)

class fibTitForTat(axl.Player):
    """
    A strategy that by default follows the rules of Tit For Tat, that
    is the player begins by cooperating, and then mimics the previous
    move made by the opponent, but has a chance of defecting each turn
    after the first turn determined by a 1-in-the Fibonacci number of the
    current turn count chance. 
    """

    # These are various properties for the strategy
    name = "fibTitForTat"
    classifier = {
        "memory_depth": 1,  # Four-Vector = (1.,0.,1.,0.)
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }
    turnCount = 0
    def strategy(self, opponent):
        self.turnCount += 1
        """This is the actual strategy"""
        # First move
        if not self.history:
            return C
        
        # Each turn, fibTitForTat has a chance of defecting outright
        # as determined by a one-in-fib(turnCount) chance
        fibChance = fib(self.turnCount)
        if getRandom(fibChance) == True:
            return D

        # React to the opponent's last move
        if opponent.history[-1] == D:
            return D
        return C
