import random
import tkinter as tk
from tkinter import messagebox

# глобальний масив
array = []


def create_array():
    global array
    array = [random.randint(-100, 100) for _ in range(200)]
    show_array()


def show_array():
    if not array:
        output.delete(1.0, tk.END)
        output.insert(tk.END, "Масив ще не створено.\n")
        return

    output.delete(1.0, tk.END)
    output.insert(tk.END, "Масив (200 елементів):\n")
    output.insert(tk.END, str(array) + "\n")


def filter_positive():
    if not array:
        messagebox.showwarning("Помилка", "Спочатку створіть масив.")
        return

    positives = [x for x in array if x > 0]

    output.delete(1.0, tk.END)
    output.insert(tk.END, "Додатні числа:\n")
    output.insert(tk.END, str(positives) + "\n")


def replace_negative():
    global array

    if not array:
        messagebox.showwarning("Помилка", "Спочатку створіть масив.")
        return

    array = [x if x >= 0 else 0 for x in array]

    output.delete(1.0, tk.END)
    output.insert(tk.END, "Масив після заміни від'ємних на 0:\n")
    output.insert(tk.END, str(array) + "\n")


def calculate_average():
    if not array:
        messagebox.showwarning("Помилка", "Спочатку створіть масив.")
        return

    avg = sum(array) / len(array)

    output.delete(1.0, tk.END)
    output.insert(tk.END, f"Середнє значення: {avg:.2f}\n")


# GUI
root = tk.Tk()
root.title("ДЗ 2 – Маски та фільтри")
root.geometry("600x450")

pink = "#FFD1DC"
root.configure(bg=pink)

label = tk.Label(root, text="Робота з масками та фільтрами",
                 font=("Arial", 14), bg=pink)
label.pack(pady=10)

frame = tk.Frame(root, bg=pink)
frame.pack(pady=10)

btn_create = tk.Button(frame, text="Створити масив", width=20, command=create_array, bg="#FFF0F5")
btn_create.grid(row=0, column=0, padx=5, pady=5)

btn_show = tk.Button(frame, text="Показати масив", width=20, command=show_array, bg="#FFF0F5")
btn_show.grid(row=0, column=1, padx=5, pady=5)

btn_filter = tk.Button(frame, text="Додатні числа", width=20, command=filter_positive, bg="#FFF0F5")
btn_filter.grid(row=1, column=0, padx=5, pady=5)

btn_replace = tk.Button(frame, text="Замінити від’ємні", width=20, command=replace_negative, bg="#FFF0F5")
btn_replace.grid(row=1, column=1, padx=5, pady=5)

btn_avg = tk.Button(frame, text="Середнє значення", width=20, command=calculate_average, bg="#FFF0F5")
btn_avg.grid(row=2, column=0, padx=5, pady=5)

btn_exit = tk.Button(frame, text="Вихід", width=20, command=root.destroy, bg="#FFF0F5")
btn_exit.grid(row=2, column=1, padx=5, pady=5)

output = tk.Text(root, width=70, height=15, bg="#FFF5F7")
output.pack(pady=10)

root.mainloop()