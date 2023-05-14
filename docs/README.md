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
