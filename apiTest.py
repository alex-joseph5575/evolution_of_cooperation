# $ pip install axelrod
import axelrod as axl
# from customPlayer1 import customPlayer1


players = [s() for s in axl.demo_strategies]  # Create players
# players = [axl.TitForTat, customPlayer1]

tournament = axl.Tournament(players, seed=1)  # Create a tournament
results = tournament.play()  # Play the tournament
results.ranked_names

print(results.wins) 
print()
print(results.ranked_names)
