###########################################
#  Example of building a custom strategy  #
###########################################

# Import the axelrod library
import axelrod as axl

# this allows us to use return C or D instead of return axl.Action.C or axl.Action.D
# from the strategy function
C, D = axl.Action.C, axl.Action.D

# This strategy is the same as cooperator
class MyStrategy(axl.Player):
    name = "My Strategy"
    # classifier = {
    #     'memory_depth': 0,
    #     'stochastic': False,
    #     'long_run_time': False,
    #     'inspects_source': False,
    #     'manipulates_source': False,
    #     'manipulates_state': False,
    # }

    def strategy(self, opponent):
        return C

####################################
# Start of creating the tournament #
####################################

# these imports are importing from the directory we are in
from test_strategy import TestStrategy
from src.custom_strats import *

tournament = axl.Tournament(
    players=[axl.Cooperator(), axl.Defector(), MyStrategy(), TestStrategy(), customPlayer1(), chaotic_clairvoyant()],
    turns=200,
    repetitions=10,
)

results = tournament.play()

print(results.ranked_names)
