# Developer README

## Project Overview

This project is a command-line number guessing game written in Python. It uses the built-in `random` module to generate numbers and provides three difficulty levels with different number ranges and attempt limits.

## Project Structure

```text
.
└── guessing_game.py
```

## Development Setup

### Requirements

* Python 3.x
* No external dependencies

### Running Locally

Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd <repository-folder>
```

Run the game:

```bash
python guessing_game.py
```

## Current Implementation

The game first asks the user to select a difficulty level.

### Difficulty Configuration

```text
Easy
- Range: 1–50
- Attempts: 10

Medium
- Range: 1–100
- Attempts: 7

Hard
- Range: 1–500
- Attempts: 5
```

The selected difficulty determines the number range and number of iterations in the corresponding `for` loop.

## Dependencies

The project only uses Python's standard library:

```python
import random
```

No package installation or virtual environment is required.

## Development Notes

The current implementation can be improved in several areas:

* Convert user input from `str` to `int` before comparing it with the generated number.
* Generate the target number once per game instead of generating a new number on every attempt.
* Add input validation for invalid or non-numeric input.
* Provide "too high" and "too low" feedback.
* Display remaining attempts.
* Handle invalid difficulty selections explicitly.
* Separate game logic into functions for better maintainability.

## Future Development

The intended direction of the project is to make the game more robust and modular while keeping it beginner-friendly. Future versions can introduce functions, validation, scoring, replay functionality, and improved user feedback.

## Development Goal

This project is primarily intended as a Python practice project for learning:

* Conditional statements
* Loops
* User input
* Functions
* Random number generation
* Basic program structure and game logic
