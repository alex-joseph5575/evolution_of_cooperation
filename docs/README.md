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

## The Project Itself
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

### Contributors
* [Alex Joseph](https://github.com/alex-joseph5575)
* [Austin Simpson](https://github.com/Austin-Simpson)
* [Marc Domingo](https://github.com/MNGSunday)
* [Jaden Suh](https://github.com/JadenSuh)
