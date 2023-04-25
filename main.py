print("importing...")
from src.custom_strats import *
from src.misc_functions import *
from src.strategy_descriptions import *
from src.functions import *
import axelrod as axl
print("Done.")
# This imports all files in the src folder

# run a basic tournament
players = [axl.Cooperator(), axl.Defector(),
           axl.TitForTat(), axl.Grudger(), example()]
tournament = axl.Tournament(players, turns=10, repetitions=3)

results = tournament.play()

df = pd.DataFrame(results.summarise())

outputToCsv(df)

