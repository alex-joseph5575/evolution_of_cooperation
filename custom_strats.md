# evolution_of_cooperation
## THIS IS NO LONGER RELEVANT FOR US
Note for adding a strategy:
follow the video, but add `from custom_strats import *` in the _strategies.py file instead of adding `from grumpy import *` to  __init__.py
The strategy list is at the bottom of the _strategies.py file instead of at the bottom of the __init__.py file. Add the class to list, not the name of the python file
adding a strategy:
https://www.youtube.com/watch?v=5kOUVdktxAo


axelrod folder (for me) is located at:
C:\Users\[username]\AppData\Local\Programs\Python\Python310\Lib\site-packages\

Add the file `custom_strats.py` to the strategies folder within the axelrod folder

Add the following line in the `_strategies.py` file in the same folder:
`from .custom_strats import customPlayer1`
and any other user created functions in that folder.

Under the list of all strategies in the `_strategies.py` file at the bottom, add any strategies created by the user

place the following file under the axelrod folder and run after creating strategies
https://github.com/Axelrod-Python/Axelrod/blob/dev/rebuild_classifier_table.py

