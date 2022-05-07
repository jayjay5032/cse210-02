# The Hilo game
---
Hilo game. Each player starts with 300 points. At each turn, a hilo program presents a card number from 1 to 13. The user guess if the next card drawn will be higher or lower than that. If the player guessed right, s/he gains 100 points. If guessed wrong s/he loses 75 points. A player who reaches 0 point loses. At each turn a player that has more than 0 point can decide whether to continue with the game or not.

## Getting Started
You will need Python 3.8.0 or newer installed and running on your computer. Then please open a terminal and browse to the project´s root folder.
Please start the program running the next command.
```
python3 Hilo
```
From Visual Studio Code you also can run the program. Start VSC and open the project folder. Go to the main module inside Hilo folder and click the ‘run’ folder button.

## computer specification
---
Python 3.8.0 or newer is required to play the game. The player can also choose to play the game on Visual Studio Code.

## Project structure

---
The project files and folders are organized as follows:
```
root                                                (project root folder)
+-- Hilo                                            (source code for game)
    +-- game                                        (specific classes folder)
        +--card.py                                  (card objest class)            
            +--constructor 
                +--value
            +--draw
                +--value = random from 1 to 13 
        +--play.py                                  (play object class)
            +--constructor
                +--is_playing
                +--score
                +--total_score
            +--start_game
            +--get_playing_consent
            +--get_guesses
            +--do_updates
            +--do_outputs           
    +-- __main__.py                                  (program entry point)
+-- README.md                                        (general info)
```

## Required Technologies
---
* Python 3.8.0

## Authors
---
* Ruei-Han Chang (cha16007@byui.edu)
* Junhee Hays (mjh226@byui.edu)
* Jesica Gutierrez (gut16002@byui.edu)
