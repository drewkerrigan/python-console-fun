#!/usr/bin/python3

import os
import time

# Define the screen's dimensions
screen_width = 100
screen_height = 20

player = "O"
player_x = 10
player_y = 10

rows = []

# Populate the sreen with spaces
for y in range(0, screen_height):
    this_row = []
    for x in range(0, screen_width):
        if x == player_x and y == player_y:
            this_row.append(player)
        else:
            this_row.append(" ")
    rows.append(this_row)

# Draw the screen 10 times with a 0.5 second pause in between frames
# Every other frame, change the direction of the "player"
for i in range(0, 10):
    os.system('clear')
    for y in range(0, screen_height):
        print('.', end='')
        for x in range(0, screen_width):
            print(rows[y][x], end='.')
        print(" ")
    time.sleep(0.1)
    rows[player_y][player_x] = " "
    if i % 2 == 0:
        player_x += 1
    else:
        player_y += 1
    rows[player_y][player_x] = player
