import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x325")

def convert_temperature():
    try:
        temp = float(temperature.get())
        unit = units.get()
        results = ""
        if unit == "Celcius":
            results += f"Temperature in Fahrenheit: {temp * 9/5 + 32:.2f}\n"
            results += f"Temperature in Kelvin: {temp + 273.15:.2f}\n"
        elif unit == "Fahrenheit":
            results += f"Temperature in Celsius: {(temp - 32) * 5/9:.2f}\n"
            results += f"Temperature in Kelvin: {(temp - 32) * 5/9 + 273.15:.2f}\n"
        elif unit == "Kelvin":
            results += f"Temperature in Celsius: {temp - 273.15:.2f}\n"
            results += f"Temperature in Fahrenheit: {(temp - 273.15) * 9/5 + 32:.2f}\n"
        else:
            results = "Invalid unit selected. Please try again."
        result.config(text=results)
    except ValueError:
        result.config(text="Please enter a number.")

label=tk.Label(root, text="Enter Temperature:")
label.pack(pady=5)
temperature=tk.Entry(root)
temperature.pack(pady=5)

units=ttk.Combobox(root, values=["Celcius", "Fahrenheit", "Kelvin"])
units.set("Select unit")
units.pack(pady=5)

convert=tk.Button(root, text="Convert", command=convert_temperature)
convert.pack(pady=10)

result=tk.Label(root, text="")
result.pack(pady=5)

root.mainloop()
