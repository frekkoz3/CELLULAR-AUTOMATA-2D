# Escape from 2DCA

A small project exploring **2D cellular automata** and turning them into a simple grid-based survival game.

This repository contains both:

* exploratory notebooks for understanding cellular automata
* a minimal game built on top of them

---

## Repository Structure

```bash
.
├── notebooks/   # Simple experiments with 2D cellular automata
└── src/         # Game implementation
```

### `notebooks/`

This folder contains lightweight notebooks that implement and visualize basic **2D cellular automata**.

They are meant for:

* experimentation
* visualization
* understanding the rules behind the automata used in the game

---

### `src/`

This folder contains the actual game logic.

The game is built around a **dynamic grid** driven by a cellular automaton.

---

## The Game

### Goal

Start from one corner of the grid and reach the opposite corner while avoiding **hazard cells**.

### Core Mechanics

* The grid evolves according to a **2D cellular automaton**
* Hazard cells correspond to the **alive cells** of the automaton
* The environment changes over time
* You must plan your path while the grid evolves
* There are some fixed safe cells that you can stay on along the path

### Gameplay Loop

Firstly there is an idle phase where you select from a visual interface the cells that are initially alive. Once this is done, the game begins.

1. You spawn in one corner of the grid
2. The cellular automaton evolves step-by-step
3. Hazard cells appear and move according to the rule
4. You try to reach the opposite corner without getting trapped

---

## 🧠 Idea Behind the Project

This project started as a simple exploration of cellular automata and evolved into a small experiment:

> What happens if the environment itself is dynamic?

Instead of static obstacles, the world changes over time, forcing the player to:

* adapt
* plan ahead
* react to emergent patterns

---

### Quick setup

Before running the actual game, insert the following commands in the terminal:

```bash
py -3.12 -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

This is the *Windows version*. Python version $\leq$ 3.12 is strongly reccomended for Pygame.

---

### Run the game

Navigate to the `src/` folder and run the main script (adjust depending on your entry point):

```bash
py main.py
```

Makes sure to have the `.venv` active.

---

## 📜 License

Feel free to use, modify, and experiment with this project.
