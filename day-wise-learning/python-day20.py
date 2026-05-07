"""
DAY 20 — OOP PROJECT STRUCTURING + SNAKE GAME PART 1
===================================================

WHAT YOU WILL LEARN
-------------------
1. Multi-file project structure
2. OOP architecture
3. Game loops
4. Object communication
5. Event listeners
6. State management
7. Turtle graphics game development

WHY THIS DAY IS IMPORTANT
-------------------------
This day teaches REAL software architecture.

Instead of writing everything in one file,
you now split logic into multiple files/modules.

This is how real-world software is built.

Future AI projects will also use this structure:

app/
    api.py
    rag.py
    embeddings.py
    agents.py
    retriever.py

TODAY'S GAME
-------------
You will build:
- Snake body
- Snake movement
- Keyboard controls
- Continuous game loop

Later days will add:
- Food
- Scoreboard
- Collision detection
- Game over logic

PROJECT STRUCTURE
-----------------
Create TWO files:

1. main.py
2. snake.py

IMPORTANT:
-----------
This single file contains BOTH code files
for learning purposes.

You must split them into separate files
inside your project folder.

===========================================================
======================== main.py ==========================
===========================================================
"""

# ==========================
# IMPORTS
# ==========================

from turtle import Screen
from snake import Snake
import time

# ==========================
# SCREEN SETUP
# ==========================

screen = Screen()

# Create game window
screen.setup(width=600, height=600)

# Background color
screen.bgcolor("black")

# Window title
screen.title("Snake Game")

"""
screen.tracer(0)

Turns OFF automatic screen updates.

Why?

Without this:
- every tiny movement is rendered
- animation becomes laggy

With tracer(0):
- we manually refresh screen
- smoother animation
- proper game engine behavior
"""

screen.tracer(0)

# ==========================
# CREATE SNAKE OBJECT
# ==========================

snake = Snake()

# ==========================
# KEYBOARD CONTROLS
# ==========================

"""
screen.listen()

Allows screen to listen for keyboard input.
"""

screen.listen()

"""
screen.onkey(function, "Key")

Calls a function when key is pressed.
"""

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# ==========================
# GAME LOOP
# ==========================

"""
Every game engine works like this:

while running:
    update()
    render()
"""

game_is_on = True

while game_is_on:

    """
    screen.update()

    Manually refreshes screen.

    VERY IMPORTANT when using tracer(0)
    """

    screen.update()

    """
    time.sleep(0.1)

    Controls game speed.

    Lower value = faster snake
    Higher value = slower snake
    """

    time.sleep(0.1)

    # Move snake continuously
    snake.move()

# Keeps window open
screen.exitonclick()

"""
===========================================================
======================== snake.py =========================
===========================================================

IMPORTANT:
-----------
Copy everything below into snake.py
"""

from turtle import Turtle

# ==========================
# CONSTANTS
# ==========================

"""
Initial snake body positions.

Each tuple represents:
(x-coordinate, y-coordinate)
"""

STARTING_POSITIONS = [
    (0, 0),
    (-20, 0),
    (-40, 0)
]

# How far snake moves each step
MOVE_DISTANCE = 20

# ==========================
# SNAKE CLASS
# ==========================

class Snake:

    """
    Snake class manages:
    - snake body
    - movement
    - direction
    - snake state
    """

    def __init__(self):

        """
        self.segments

        Stores ALL snake body parts.
        """

        self.segments = []

        """
        Create initial snake body.
        """

        for position in STARTING_POSITIONS:
            self.add_segment(position)

        """
        Snake head is first segment.
        """

        self.head = self.segments[0]

    # ==========================
    # CREATE NEW SEGMENT
    # ==========================

    def add_segment(self, position):

        """
        Creates ONE snake body segment.
        """

        segment = Turtle("square")

        # Snake color
        segment.color("white")

        """
        penup()

        Prevents drawing lines while moving.
        """

        segment.penup()

        # Move segment to position
        segment.goto(position)

        # Add segment to snake body list
        self.segments.append(segment)

    # ==========================
    # MOVE SNAKE
    # ==========================

    def move(self):

        """
        Snake movement logic:

        Tail follows body.
        Body follows head.

        IMPORTANT:
        We move BACKWARDS.

        Example:
        Segment 2 copies segment 1 position
        Segment 1 copies segment 0 position
        Head moves forward
        """

        for seg_num in range(len(self.segments) - 1, 0, -1):

            # Get previous segment coordinates
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()

            # Move current segment
            self.segments[seg_num].goto(new_x, new_y)

        # Move head forward
        self.head.forward(MOVE_DISTANCE)

    # ==========================
    # DIRECTION METHODS
    # ==========================

    """
    Heading Angles:

    0   -> Right
    90  -> Up
    180 -> Left
    270 -> Down
    """

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)

"""
===========================================================
======================= IMPORTANT NOTES ===================
===========================================================

1. WHY USE CLASSES?
-------------------
Classes organize code properly.

Snake class manages:
- movement
- body
- direction

main.py only controls game flow.

This is called:
ENCAPSULATION

2. WHY USE MULTIPLE FILES?
--------------------------
Real software is NEVER one huge file.

Large systems are split into modules.

Example AI project:

app/
    agents.py
    llm.py
    vector_db.py
    retriever.py

3. GAME LOOP CONCEPT
--------------------
This is how ALL games work:

while game_running:
    update()
    render()

Even:
- Unity
- Unreal Engine
- Pygame

4. COMMON BUGS
---------------
BUG 1:
Forgetting screen.update()

BUG 2:
Forgetting self in methods

BUG 3:
Moving snake incorrectly

Correct approach:
Move from BACK to FRONT

5. IMPORTANT OOP CONCEPTS
-------------------------
- Classes
- Objects
- Methods
- Encapsulation
- State management
- Object communication

6. REAL INDUSTRY CONNECTION
---------------------------
Today's architecture maps directly to:

Snake Game        -> AI Systems
-----------------------------------------
Snake class       -> Agent class
move()            -> execute()
segments          -> memory states
game loop         -> event loop
keyboard input    -> API requests
screen update     -> frontend render

===========================================================
======================= MINI EXERCISES ===================
===========================================================

1. Change snake color
2. Increase speed
3. Add more segments
4. Use circle shapes instead of square
5. Print coordinates while moving

===========================================================
========================= DAY 21 ==========================
===========================================================

Tomorrow you will add:

- Food
- Snake growth
- Collision detection
- Scoreboard
- Game over system

The game becomes FULLY PLAYABLE.

===========================================================
END OF DAY 20
===========================================================
"""