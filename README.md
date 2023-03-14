# evolution_of_cooperation

adding a strategy:
https://www.youtube.com/watch?v=5kOUVdktxAo


note: We may need to have the dev branch of the github
https://github.com/Axelrod-Python/Axelrod


axelrod folder located at:
C:\Users\[username]\AppData\Local\Programs\Python\Python310\Lib\site-packages

Add the file `custom_strats.py` to the strategies folder within the axelrod folder

Add the following line in the `_strategies.py` file in the same folder:
`from .custom_strats import customPlayer1`
and any other user created functions in that folder.

Under the list of all strategies in the `_strategies.py` file at the bottom, add any strategies created by the user

place the following file under the axelrod folder and run after creating strategies
https://github.com/Axelrod-Python/Axelrod/blob/dev/rebuild_classifier_table.py

writing test for user created files:
https://axelrod.readthedocs.io/en/stable/how-to/contributing/strategy/writing_test_for_the_new_strategy.html?highlight=create

adding new strategy
https://axelrod.readthedocs.io/en/stable/how-to/contributing/strategy/adding_the_new_strategy.html
