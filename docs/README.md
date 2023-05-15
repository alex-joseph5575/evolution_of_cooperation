# Evolution of Cooperation

## Introduction
### What is the Prisoner's Dilemma?
The Prisoner's Dilemma is a thought experiment in game theory in which two prisoners are given the opportunity to either sell out the other prisoner (betrayal) or to remain silent (cooperate). 

For the prisoners, there exists four possible outcomes for the scenario:

- If both prisoners cooperate, both prisoners receive a 2-year sentence
- If both prisoners betray each other, both prisoners receive a 5-year sentence
- If one prisoner betrays while another prisoner cooperates:
	
	- The prisoner who betrayed the other goes free
	- The prisoner who cooperated, and was thus stabbed in the back, receives a 10-year sentence.

With the outcomes of the Prisoner's Dilemma in mind, it would make no sense to blindly cooperate with the other prisoner, as in the best-case scenario, betraying the other prisoner allows the individual to go free while the worst-case scenario for betraying is a 5-year sentence. Meanwhile, cooperating has a best-case scenario of only having a 2-year sentence, while having the worst worst-case scenario of a 10-year sentence after being betrayed.  

This project seeks to look into a variation of the Prisoner's Dilemma called the Iterative Prisoner's Dilemma in which multiple rounds of the Prisoner's Dilemma are played sequentially, meaning that both prisoners will remember each others' decisions during previous rounds. Compared to the normal Prisoner's Dilemma, the Iterative Prisoner's Dilemma provides additional incentive to cooperate with the other prisoner due to the iterative variant of the scenario representing an ongoing relationship of trust and betrayal between the two prisoners.


### Why is this interesting?
Examining the behaviors and outcomes of the "prisoners" involved within the Prisoner's Dilemma enables us to examine human biases within relationships, such as why humans are biased towards cooperating with each other, even when an incentive to be selfish provides a better outcome. In addition to this, the Iterative Prisoner's Dilemma asks additional questions in Social Psychology such as "Why do humans trust each other when it makes more logical sense to distrust?" and "When do the repercussions for acting selfishly get outweighed by the benefits?"

## Literature Review
### Regarding the Prisoner's Dilemma
[Effective Choice in the Prisoner's Dilemma (Axelrod 1980)](https://www.jstor.org/stable/173932)

The Prisoner's Dilemma itself is a widely-examined topic within the field of Social Psychology in that it encapsulates an individual's internal conflict between Individual Rationality and Group Rationality when making decisions.

- Individual Rationality advocates for acting selfishly as in the scenario of the Prisoner's Dilemma, betraying the other prisoner provides arguably better outcomes than cooperating with the other prisoner

	- In the base Prisoner's Dilemma, the other prisoner's motives and willingness to either betray or cooperate are unknown, and because of this, defecting provides relatively better outcomes than blind trust
	- In the case of the Iterative Prisoner's Dilemma, the individual is still subject to uncertainty due to the other prisoner randomly deciding to betray on a whim

- Group Rationality advocates for acting in the best interest of everyone and thus what would benefit the entire group the most, which in the case of the Prisoner's Dilemma is trusting the other prisoner to cooperate regardless of uncertainty

	- In the base Prisoner's Dilemma, Group Rationality argues for cooperating in the event that the other prisoner also wants to act in the best interest for the group, but ultimately has the worst outcome possible if the individual is betrayed
	- In the case of the Iterative Prisoner's Dilemma, the incentive to cooperate with the other prisoner is heightened as the other prisoner will remember actions from previous rounds, which represents an ongoing relationship between the two prisoners

### An Overview of the First Axelrod Tournament
[Effective Choice in the Prisoner's Dilemma (Axelrod 1980)](https://www.jstor.org/stable/173932)

As at the time, Axelrod had noticed that only the base variant of the Prisoner's Dilemma had been examined through research, but not the Iterative Prisoner's Dilemma, Axelrod had conducted a tournament in order to examine what strategy would perform the best when confronted against others in an Iterative Prisoner's Dilemma Tournament.

The tournament itself:

- Consisted of 15 Strategies that were submitted by economists, psychologists, sociologists, mathematicians, and political scientists
- Was styled as a Round Robin Tournament, meaning that each strategy faced each other in a 1-on-1 match during the tournament

	- Each match of the tournament lasted 200 rounds

- Had a point breakdown of:

	- 3 Points awarded to both strategies in the event of mutual cooperation (C, C)
	- 1 Point awarded to both strategies in the event of mutual defection (D, D)
	- And in the case where one strategy cooperated and the other strategy defected (C, D)

		- The strategy that defected (D) receives 5 points
		- The strategy that cooperated (C) recieves 0 points

The most successful strategy within the original Axelrod Tournament was the strategy [Tit For Tat](https://github.com/Axelrod-Python/Axelrod/blob/master/axelrod/strategies/titfortat.py), a strategy that begins by cooperating (C) with the opponent strategy until the opponent defects (D). Tit For Tat would then defect (D) the turn following after the opponent's defection (D), and then continue cooperating (C) until the opponent defects (D) again. In spite of not only being a basic strategy, but also a strategy that other participants in the tournament had submitted variations of in order to attempt to "improve" it, Axelrod had noticed a trend in Tit For Tat and other strategies that had performed well during the tournament.

Axelrod had noticed that strategies that scored high during Iterative Prisoner's Dilemma were:

- **Nice**. The strategies did not begin nor end each match by defecting (D), and overall prioritized cooperating (C) with the opposing strategy.
- **Effective in matches against specific strategies**. Axelrod had noticed two strategies that performed exceptionally well in the tournament, and had noticed that high-scoring strategies had also worked well when competing against these strategies:

	- **DOWNING**. A strategy that attempts to predict its opponents next move based on how DOWNING had acted during the previous turn.

		- For example, if DOWNING determines that a strategy, such as Tit For Tat, tends to cooperate (C) unless DOWNING defects (D), then DOWNING will determine that cooperating (C) is the best action to take on subsequent rounds of the match. Conversely, if DOWNING determines that a strategy tends to defect (D) often regardless of DOWNING's actions, DOWNING determines that the best course of action is to defect (D) on subsequent rounds of the match.

	- **GRAASKAMP**. A strategy that attempts to determine whether it is facing Tit For Tat, a variant of Tit For Tat, or a strategy that cooperates (C) and defects (D) randomly.

		- GRAASKAMP initially starts off as Tit For Tat for the first 50 turns for the match, and then Defects. If GRAASKAMP is facing off against Tit For Tat or a variant, after a defect (D) from the opponent on the 52nd turn, then GRAASKAMP continues to play Tit For Tat for the rest of the match. If GRAASKAMP determines that its own score is bad by the 52nd turn, it assumes that the opponent is defecting (D) and cooperating (C) randomly, and thus decides to defect (D) for the rest of the match.

- **Forgiving**. The strategies did not excessively (at most once or 0 times) punish the opponent by defecting (D) after the opponent had defected (D) during the previous round.  


## The Project Itself
The objective of this project was to take the already existing [Axelrod API](https://github.com/Axelrod-Python/Axelrod/tree/master), and make it a lot more-user friendly with an easier program to run tournaments and 1-on-1 matches with various options to display the results of said tournaments and matches, in addition to including a template on how to implement user-made custom strategies.

### Installation Instructions
First, clone the repository:
```
git clone https://github.com/alex-joseph5575/evolution_of_cooperation.git
```
Then run the following in the command line. 
```
pip install axelrod
```

### Quickstart Instructions
To start the program, enter the following in the command line:
```
python main.py
```
This will prompt a basic command line interface that you can follow to set up a prisoner's dilemma competition. Once you have selected your strategies, the tournament will commence. 

### Tournament Variables

#### Rounds
The maximum number of rounds that each match in the tournament itself can be played.
A randomized number of rounds will also be added to the inputted number.
Current maximum allowable rounds is 100 to avoid excessively long tournaments.

#### Noise
The probability that a player's move will be flipped between C and D. This random flip occurs in every round of every match at the given probability.
A maximum of 1 noise will result in every move being the opposite of what the strategy determines.

#### Probabilistic Ending
The probability that a match in a tournament will end after the given round. This chance to prematurely end the match will occur in every round of every match at the given probability.
A maximum of 0.5 probabilistic end can be given for a 50% chance that each match ends after every round.

#### Transformations
Transformations alter strategies in specific ways. Each strategy can only be transformed once and the strategy's name will be altered to reflect the transformation.
If every strategy is transformed once, the program will begin the tournament without input from the user.
Currently implemented transformers:
* Flip Transformer: All of the strategy's moves will be the opposite of what they should be. Effectively 100% noise.
* Deadlock Breaking Transformer: The strategy will attempt to break alternating (defect, cooperate), (cooperate, defect) deadlocks by cooperating on its next chance to defect.
* Retaliate Until Apology Transformer: Applies tit-for-tat style retaliation where the strategy will defect upon betrayal until the opponent cooperates.
* Noisy Transformer: Allows for the application of noise to an individual strategy instead of the entire tournament. 
	* Noisy Transformer will only be available for matches and tournaments with no noise.

### Documentation
Project was built upon the Axelrod API in Python, consisting of an overall looping program logic containing initial strategy selection, parameter manipulation, and output options in that order. Two custom strategies - Chaotic Clairvoyant and FibTitForTat - were implemented. Chaotic Clairvoyant takes advantage of a high memory depth, while FibTitforTat uses the fibonacci sequence to create a high amount of randomization.

### Contributors
* [Alex Joseph](https://github.com/alex-joseph5575) - Project leader, assigned tasks and checked progress, contributed to research, program logic, and output creation
* [Austin Simpson](https://github.com/Austin-Simpson) - Created output logic and implemented plotting tools, implemented custom strategy feature
* [Marc Domingo](https://github.com/MNGSunday) - Researched related literature and implemented strategy list with explanations
* [Jaden Suh](https://github.com/JadenSuh) - Implemented user-selected parameters such as noise and evolved strategies, created general program logic

### Testing
Testing was done via comparison to scripts written solely with the Axelrod API, and by testing several possible branches inside the program. By comparing data received from our program to the data output given by the API, we were able to verify that our program is functioning properly and not mistranslating the data received from the API.

### Results and Future Development
The entire program is functional to the best of our knowledge. Plans changed dramatically upon discovery of the API, shifting from creating our own tournament to building upon the API's existing work. All project goals have been accomplished, but there are many ways in which it can be improved upon in the future: 
* Foremost among them would be a GUI, implemented alongside the existing program logic to provide a much easier to use graphical interface as opposed to one based in the command line. Existing GUI packages would be the simplest to leverage to achieve this goal.
* Another goal would be to further reduce the coding necessary for custom strategies, as some scripting knowledge is still necessary at this time. 
* Additional games such as the Guardian's Dilemma and Helping Game could be implemented alongside the Prisoner's Dilemma by changing the accepted actions.
* Add strategy evolution throughout the tournament by making use of the moran process function from the axelrod API. It's addition would involve similar work to our project where the scope of the moran process would need to be determined and UI additions would need to be made to add a layer of abstraction to simplify the setup and output for users.
* Turning the program into a playable game. This could be done by adding a "player" strategy that when included in the tournament, allows a player to input the moves manually for each round. The player would have access to the match history of each match they're playing so they can both try to identify what strategy their playing against and make optimal moves against the opponent. The program could also compare the user's overall move selection to the list of strategies to tell the user if they chose moves similarly to an implemented strategy.

