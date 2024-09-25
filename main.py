import tkinter as tk
import numpy as np
np.set_printoptions(threshold = np.inf)

def draw_line(event):
    global line_id
    line_points.extend((event.x, event.y))
    if line_id is not None:
        drawing.append([event.x,event.y])
        canvas.delete(line_id)
    line_id = canvas.create_line(line_points, **line_options)

def set_start(event):
    line_points.extend((event.x, event.y))

def end_line(event=None):
    global line_id
    line_points.clear()
    line_id = None

size = 100
line_id = None
line_points = []
line_options = {}
drawing = []
root = tk.Tk()
canvas = tk.Canvas(width=size, height=size)
canvas.pack()
canvas.bind('<Button-1>', set_start)
canvas.bind('<B1-Motion>', draw_line)
canvas.bind('<ButtonRelease-1>', end_line)
root.mainloop()

def print_matrix(input_matrix):
    for i in range(0,size):
        print(input_matrix[i])

matrix = []
for i in range(0,size):
    row = []
    for j in range(0,size):
        row.append(0)
    matrix.append(row)

for i in range(0,len(drawing)):
    try:
        matrix[drawing[i][1]][drawing[i][0]] = 1
    except:
        pass

print_matrix(matrix)