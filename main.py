from src.custom_strats import *
from src.misc_functions import *
from src.strategy_descriptions import *
import axelrod as axl

# This imports all files in the src folder

tournament = axl.Tournament(
    players=[axl.Cooperator(), axl.Defector(), example()],
    turns=200,
    repetitions=10,
)


