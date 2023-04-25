# Adding a custom strategy

To add a custom strategy, add another function to the `custom_strats.py` file. The function should take two arguments, `player` and `opponent`, and return either `C` (Cooperate) or `D` (Defect). Note that you are not returning a string, but rather the actual `C` or `D` character.

There is an example strategy as the first class in the file. You can use this as a template, but make sure to change the class name. The class name is used to identify the strategy in the UI.