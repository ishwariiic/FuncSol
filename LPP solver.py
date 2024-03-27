import tkinter as tk
from tkinter import Label, Entry, Button, Text
import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

def solve_lp_problem():
    c = [float(c_i.get()) for c_i in c_entries]
    A = []
    b = []
    for i in range(len(A_entries)):
        row = [float(entry.get()) for entry in A_entries[i]]
        A.append(row)
        b.append(float(b_entries[i].get()))

    if problem_type.get() == "Maximize":
        c = [-x for x in c]

    result = linprog(c, A_ub=A, b_ub=b, method="highs")
    result_text.config(state='normal')
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Optimal Solution:\n")
    for i, x in enumerate(result.x):
        result_text.insert(tk.END, f'x{i + 1} = {x}\n')
    result_text.insert(tk.END, f'Optimal Value: {result.fun}\n')
    result_text.config(state='disabled')

root = tk.Tk()
root.title("Linear Programming Problem Solver")


Label(root, text="Objective Function (c):").grid(row=0, column=0)
c_entries = [Entry(root) for _ in range(2)]
for i, entry in enumerate(c_entries):
    entry.grid(row=0, column=i + 1)
    entry.insert(0, "0")


Label(root, text="Constraints (A):").grid(row=1, column=0)
A_entries = []
for i in range(2):
    row_entries = [Entry(root) for _ in range(2)]
    A_entries.append(row_entries)
    for j, entry in enumerate(row_entries):
        entry.grid(row=i + 1, column=j + 1)
        entry.insert(0, "0")

Label(root, text="RHS (b):").grid(row=3, column=0)
b_entries = [Entry(root) for _ in range(2)]
for i, entry in enumerate(b_entries):
    entry.grid(row=3, column=i + 1)
    entry.insert(0, "0")


problem_type = tk.StringVar()
problem_type.set("Minimize")
Label(root, text="Select Problem Type:").grid(row=4, column=0)
minimize_radio = tk.Radiobutton(root, text="Minimize", variable=problem_type, value="Minimize")
minimize_radio.grid(row=4, column=1)
maximize_radio = tk.Radiobutton(root, text="Maximize", variable=problem_type, value="Maximize")
maximize_radio.grid(row=4, column=2)


solve_button = Button(root, text="Solve", command=solve_lp_problem)
solve_button.grid(row=5, column=0, columnspan=4)


Label(root, text="Optimal Solution:").grid(row=6, column=0)
result_text = Text(root, height=6, width=30)
result_text.grid(row=7, column=0, columnspan=4)
result_text.config(state='disabled')

root.mainloop()
