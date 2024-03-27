import tkinter as tk
import statistics
from statistics import variance
from statistics import stdev

def calculate_factorial():
    num = int(factorial_entry.get())
    if num == 0:
        factorial_result.config(text="Factorial of 0 is 1")
    elif num < 0:
        factorial_result.config(text="Factorial doesn't exist for negative numbers")
    else:
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        factorial_result.config(text=f"Factorial of {num}! is {fact}")

def calculate_statistics():
    data = data_entry.get()
    data_list = [float(x) for x in data.split()]
    data_result.config(text=f"Your given list of data elements was {data_list}")
    mean = statistics.mean(data_list)
    median = statistics.median(data_list)
    mode = statistics.mode(data_list)
    var = variance(data_list)
    st_dev = stdev(data_list)
    data_stats.config(text=f"Mean: {mean}\nMedian: {median}\nMode: {mode}\nVariance: {var}\nStandard Deviation: {st_dev}\nRange: {max(data_list) - min(data_list)}")
    


root = tk.Tk()
root.title("Factorial Calculator and Statistics Calculator")


factorial_label = tk.Label(root, text="Enter a number to calculate factorial ")
factorial_label.pack()
factorial_entry = tk.Entry(root)
factorial_entry.pack()
factorial_button = tk.Button(root, text="Calculate Factorial", command=calculate_factorial)
factorial_button.pack()
factorial_result = tk.Label(root, text="")
factorial_result.pack()


statistics_label = tk.Label(root, text="Enter list of values separated by space")
statistics_label.pack()
data_entry = tk.Entry(root, width=40)
data_entry.pack()
statistics_button = tk.Button(root, text="Calculate Statistics", command=calculate_statistics)
statistics_button.pack()
data_result = tk.Label(root, text="")
data_result.pack()
data_stats = tk.Label(root, text="")
data_stats.pack()

root.mainloop()
