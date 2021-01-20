# open-close-game
## How to run it

0. open terminal or command line
1. install python (2.7.x is recommended but 3.x is appropriate as well.)
2. Clone Repository
3. `cd open-close-game`
4. type `python open-close-game.py`
5. enjoy


# Structure

```
- /
- open-close-game.py
- /Game
  - player.py
  - game.py
```

###### Overview
This game include 3 files;
  - open-close-game.py
  - player.py
  - game.py
  

###### open-close.game.py
This is `main file` which operate all process of game. Program designed to declare 2 classes such as `Player` class and `Game` class.

###### player.py
This is `Player` assigned. It will store 
- player answer, 
- player status (predictor or not),
- automatic player (bot) will be in-function setting.

###### game.py
This is `Game` class which will operate all instruction including 
- trigger function to start game
- checking winner function (receive Player class as value)
