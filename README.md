# Harry Potter Battle Game 	:mage_man:


This project is the result of a [Code First Girls](https://codefirstgirls.com/) task, with the open-ended challenge of creating a game using an API.

<img width="172" alt="image" src="https://user-images.githubusercontent.com/106174870/184108119-2775d5e4-7e61-4baa-95ca-8f4c8d531dca.png">

## The Concept

I chose to use a [Harry Potter API](https://hp-api.herokuapp.com/) to create a spell casting battle game against a computer opponent. Players begin with 100 health and cast either damage or healing spells, with the goal of reducing your opponent’s health to 0.

## Key Features

:magic_wand: Text input for character selection via API

:magic_wand: Houses have ‘special powers’ with damage/healing modifications

:magic_wand: Random spell chosen via a [different API](https://fedeperin-harry-potter-api-en.herokuapp.com) based on healing or damage selection

:magic_wand: Text interface embellishments

:magic_wand: Filtered text input to assist user experience

:magic_wand: Modular functions for code efficiency

## How to run the game :owl:

1. Make sure you have [Python](https://www.python.org/downloads/) installed

2. Clone the repository to your desired location

    `git clone https://github.com/Cinzia-I-M/harry-potter-battle-game.git`

3. Enter the repository directory via command line

    `cd harry-potter-battle-game`

4. Run the script

    `python harrypotter.py`

5. Enjoy playing!

# Play the game!

- First you can choose if you would like to pick your team or if you want a random team.
- If you choose to pick your team,  you can select three characters from Harry Potter by typing all or part of their names.
- Depending on which house your characters are in, you will get special powers that either increase or decrease your damage and healing powers.
- The computer selects a random team.
- Then you start the battle! Pick a damage spell to start. This will harm the computer's health.
- The computer then picks either a damage or healing spell.
- This goes on until one of you reaches 0 health.
- Beware of Avada Kedavra (**The Killing Curse**) as this will kill instantly! :magic_wand:
- At the end you can choose to play again or not.
