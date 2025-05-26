from ursina import *

app = Ursina()

cube = Entity(model='cube', color=color.orange, scale=2, collider='box')

# Predefined list of colors to cycle through
colors = [
    color.red,
    color.green,
    color.blue,
    color.yellow,
    color.violet,
    color.orange,
    color.cyan,
    color.magenta
]

color_index = 0

def input(key):
    global color_index
    if key == 'left mouse down' and mouse.hovered_entity == cube:
        color_index = (color_index + 1) % len(colors)
        cube.color = colors[color_index]

app.run()
