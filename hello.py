import tkinter as tk

root = tk.Tk()

count = 0

def increase():
    global count
    count += 1
    btn.config(text=str(count))

btn = tk.Button(root, text="0", command=increase)
btn.pack()

root.mainloop()




import tkinter as tk

window = tk.Tk()

def change_color():
    button.config(bg="red")

button = tk.Button(window, text="Нажми меня", command=change_color)
button.pack()

window.mainloop()

