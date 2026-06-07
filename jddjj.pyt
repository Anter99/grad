import tkinter as tk
from tkinter import messagebox
import time

root = tk.Tk()
root.title("MiniOS")
root.attributes("-fullscreen", True)
root.configure(bg="black")

def update_time():
    current = time.strftime("%H:%M:%S")
    clock.config(text=current)
    root.after(1000, update_time)

def about():
    messagebox.showinfo("Про систему", "MiniOS v1.0\nСтворено на Python")

def exit_os():
    root.destroy()

# Верхня панель
top = tk.Frame(root, bg="gray20", height=40)
top.pack(fill="x")

clock = tk.Label(top, fg="white", bg="gray20", font=("Arial", 16))
clock.pack(side="right", padx=10)

title = tk.Label(top, text="MiniOS", fg="white", bg="gray20", font=("Arial", 16))
title.pack(side="left", padx=10)

# Робочий стіл
desktop = tk.Frame(root, bg="darkblue")
desktop.pack(fill="both", expand=True)

btn1 = tk.Button(desktop, text="Інформація",
                 width=20, height=3, command=about)
btn1.place(x=50, y=50)

btn2 = tk.Button(desktop, text="Вийти",
                 width=20, height=3, command=exit_os)
btn2.place(x=50, y=150)

update_time()
root.mainloop()