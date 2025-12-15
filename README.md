# CLI Wheel Game 🎡

A terminal-based wheel spinning game built in Python.

This project focuses on **game development fundamentals** using a CLI:
- Game loop design
- Player turns and limits
- Score tracking
- Animation illusion in terminal
- Input-driven state changes

## Game Rules
- The wheel contains numbers from 1 to 10
- Each spin lands on one number
- The player gets exactly 5 spins
- Each number adds to the total score
- Highest possible score: 50

## How It Works
1. Player presses ENTER to spin
2. The wheel animates in a spiral-like motion
3. The arrow stops on a number
4. Score updates
5. Game ends after 5 spins

## Run the Game
```bash
python wheel_game.py
