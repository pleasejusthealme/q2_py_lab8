import tkinter as tk
from tkinter import ttk, colorchooser
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

window = tk.Tk()
window.title("Graphics GUI")
window.geometry("800x600")

line_color = 'blue'

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

x = np.linspace(-10, 10, 400)

def choose_color():
    global line_color
    color = colorchooser.askcolor()[1]
    if color:
        line_color = color

def draw_graph():
    func = combo.get()
    width = scale.get()
    label = label_entry.get()

    if func == 'y = x':
        y = x
    elif func == 'y = x^2':
        y = x**2
    elif func == 'y = sin(x)':
        y = np.sin(x)
    elif func == 'y = cos(x)':
        y = np.cos(x)
    else:
        return
    
    ax.plot(x, y, color = line_color, linewidth=width, label=label)

    ax.set_title(title_entry.get())
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)

    if label != '':
        ax.legend()

    canvas.draw()

def clear_gr():
    ax.clear()
    canvas.draw()

frame = tk.Frame(window)
frame.pack(side=tk.LEFT, padx=10, pady=10)

tk.Label(frame, text='Choose function:').pack()

combo = ttk.Combobox(frame)
combo['values'] = ['y = x', 'y = x^2', 'y = sin(x)', 'y = cos(x)']
combo.current(0)
combo.pack(pady=5)

tk.Button(frame, text='Choose color:', command=choose_color).pack(pady=5)

tk.Label(frame, text='Line width:').pack()

scale = tk.Scale(frame, from_=1, to=10, orient='horizontal')
scale.set(2)
scale.pack(pady=5)

tk.Label(frame, text="Line label").pack()

label_entry = tk.Entry(frame)
label_entry.insert(0, 'Graph')
label_entry.pack(pady=5)

tk.Label(frame, text="Graph label").pack()

title_entry = tk.Entry(frame)
title_entry.insert(0, 'Graph')
title_entry.pack(pady=5)

tk.Button(frame, text='Build!', command=draw_graph).pack(pady=5)
tk.Button(frame, text='Clear!', command=clear_gr).pack(pady=5)

window.mainloop()