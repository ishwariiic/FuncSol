import tkinter as tk
import cmath
import matplotlib.pyplot as plt
import sympy as sp

def calculate_quadratic():
    a = int(a_entry.get())
    b = int(b_entry.get())
    c = int(c_entry.get())

    dis = (b ** 2) - (4 * a * c)
    ans1 = (-b - cmath.sqrt(dis)) / (2 * a)
    ans2 = (-b + cmath.sqrt(dis)) / (2 * a)

    result_label.config(text=f"The discriminant for the equation is : {dis}")
    roots_label.config(text=f"Roots for the equations are  : {ans1}, {ans2}")

def plot_linear():
    equation = equation_entry.get()

    x = sp.symbols('x')
    y = sp.sympify(equation)
    derivative = sp.diff(y, x)
    critical_point = sp.solve(derivative, x)

    x_values = []
    y_values = []

    for x_val in range(-10, 10):
        x_values.append(x_val)
        y_values.append(y.subs(x, x_val))

    plt.plot(x_values, y_values, label=f'Linear Equation: {equation}')

    for point in critical_point:
        if point.is_real:
            plt.scatter(float(point), float(y.subs(x, point)), color='red', marker='o')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


root = tk.Tk()
root.title("Quadratic Equation Solver and Linear Equation Plotter")


a_label = tk.Label(root, text="Enter value of a:")
a_label.grid(row=0, column=0, padx=10, pady=5)
a_entry = tk.Entry(root)
a_entry.grid(row=0, column=1, padx=10, pady=5)

b_label = tk.Label(root, text="Enter value of b :")
b_label.grid(row=1, column=0, padx=10, pady=5)
b_entry = tk.Entry(root)
b_entry.grid(row=1, column=1, padx=10, pady=5)

c_label = tk.Label(root, text="Enter value of c :")
c_label.grid(row=2, column=0, padx=10, pady=5)
c_entry = tk.Entry(root)
c_entry.grid(row=2, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate Quadratic", command=calculate_quadratic)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

roots_label = tk.Label(root, text="")
roots_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

equation_label = tk.Label(root, text="Enter Linear Equation (e.g., 2*x + 3):")
equation_label.grid(row=6, column=0, padx=10, pady=5)
equation_entry = tk.Entry(root)
equation_entry.grid(row=6, column=1, padx=10, pady=5)

plot_button = tk.Button(root, text="Plot Linear Equation", command=plot_linear)
plot_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)



root.mainloop()
