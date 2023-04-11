from axelrod.action import Action, actions_to_str
from axelrod.player import Player
from axelrod.strategy_transformers import (
    FinalTransformer,
    TrackHistoryTransformer,
)

C, D = Action.C, Action.D


class customPlayer1(Player):
    """
    A player starts by cooperating and then mimics the previous action of the
    opponent.
    This strategy was referred to as the *'simplest'* strategy submitted to
    Axelrod's first tournament. It came first.
    Note that the code for this strategy is written in a fairly verbose
    way. This is done so that it can serve as an example strategy for
    those who might be new to Python.
    Names:
    - Rapoport's strategy: [Axelrod1980]_
    - TitForTat: [Axelrod1980]_
    """

    # These are various properties for the strategy
    name = "customPlayer1"
    classifier = {
        "memory_depth": 1,  # Four-Vector = (1.,0.,1.,0.)
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def strategy(self, opponent: Player) -> Action:
        """This is the actual strategy"""
        # First move
        if not self.history:
            return C
        # React to the opponent's last move
        if opponent.history[-1] == D:
            return D
        return C
    
    def clone(self):
        return self
    
class chaotic_clairvoyant(Player):
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

    def strategy(self, opponent: Player) -> Action:
        """This is the actual strategy"""
        c_count = 0
        d_count = 0
        # First move
        if not self.history:
            return D
        # If opponent hasn't played 3 moves yet
        if opponent.history < 3:
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
    
    def clone(self):
        return self

