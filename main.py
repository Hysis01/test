import tkinter
import random
import time

size = 400
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=size, height=size)
canvas.pack()

colors = ["blue", "red", "black", "orange", "green", 'red', 'CadetBlue', 'DarkCyan', 'ForestGreen', 'AntiqueWhite']
circles = []
usedColor = []
for i in range(5):
    a = random.randint(-10, -1)
    b = random.randint(1, 10)
    oval = {'dx': a, 'dy': b}
    y = x = random.randint(101, size - 101)
    d = random.randint(10, 100)
    y1 = x1 = x + d
    color = random.choice(colors)
    while usedColor.__contains__(color):
        color = random.choice(colors)
    usedColor.append(color)
    oval['id'] = canvas.create_oval(x, y, x1, y1, fill=color)

    circles.append(oval)

while True:
    for i in circles:
        x, y, x1, y1 = canvas.coords(i['id'])
        if x < 1 or x1 > size - 1:
            i['dx'] = -i['dx']
        elif y < 1 or y1 > size - 1:
            i['dy'] = -i['dy']
        canvas.move(i["id"], i["dx"], i["dy"])
    canvas.update()
    time.sleep(0.05)
