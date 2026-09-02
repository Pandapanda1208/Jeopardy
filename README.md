# 🎲 Python Pygame Jeopardy

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Pygame](https://img.shields.io/badge/Pygame-Ready-green?style=flat&logo=python)

## 📝 Description
An interactive, fully playable Jeopardy game board built entirely in Python using the `pygame` library. This project allows you to play a full game of Jeopardy—complete with Single Jeopardy, Double Jeopardy, Daily Doubles, and Final Jeopardy! 

Instead of hardcoding questions into the script, the game dynamically loads all categories, point values, questions, and answers from a simple JSON file (`Jeopardy_data.json`). This makes it incredibly easy to host your own trivia nights with completely custom topics!

## ✨ Features
* **Full Game Flow:** Includes a first board (Single Jeopardy), a second board (Double Jeopardy), and a Final Jeopardy sequence.
* **Interactive UI:** Click on a tile to reveal the question, click again to see the answer, and click a third time to return to the board (the completed tile will grey out).
* **Data-Driven Customization:** Easily swap out categories, questions, and answers by editing the included `Jeopardy_data.json` file.
* **Daily Doubles:** Built-in support for hidden Daily Double questions.
* **Audio Support:** Automatically loops a background theme song (`Jeopardy Theme.wav`) during gameplay.
* **Fullscreen & Scaled:** Runs in a dynamic fullscreen 1366x768 scaled resolution.

## 🚀 Getting Started

### Prerequisites
To run this game, you will need **Python 3.x** installed on your computer, along with the `pygame` library.

Install Pygame via pip:
```bash
pip install pygame
