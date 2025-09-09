# Text-Based RPG Battle Simulator

This is a simple Python text-based RPG battle simulator. A player and an enemy take turns attacking each other, reducing each other's HP until one is defeated. The winner is declared at the end of the battle.

## Features

- Turn-based combat between player and enemy
- Randomized damage for each attack
- HP tracking and winner announcement

## How to Run

1. Make sure you have Python 3 installed.
2. Save `battle_simulator.py` to your computer.
3. Run the script from the command line:

```bash
python battle_simulator.py
```

## Example Output

```
Battle Start!
Player HP: 30 | Enemy HP: 25

Player attacks Enemy for 7 damage!
Player HP: 30 | Enemy HP: 18

Enemy attacks Player for 5 damage!
Player HP: 25 | Enemy HP: 18

...
Player wins!
```

## Customization

- You can change the initial HP, attack range, and names by editing the `Character` initialization in the script.

## License

This project is open-source and free to use.
