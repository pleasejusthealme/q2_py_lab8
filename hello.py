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

import random

# генерация списка случайных чисел
numbers = [random.randint(1, 100) for _ in range(10)]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

print("Исходный список:", numbers)

sorted_numbers = insertion_sort(numbers)

print("Отсортированный список:", sorted_numbers)

