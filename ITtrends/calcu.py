import tkinter as tk

def on_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"{expression} = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Syntax and Result Display Calculator")

# Create an entry widget for input and display
entry = tk.Entry(root, width=16, font=('Arial', 16), bd=5, insertwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.',  '+'
]

# Add buttons to the grid
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, width=4, height=2, command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Add special buttons
tk.Button(root, text="C", width=4, height=2, command=clear_entry).grid(row=row_val, column=0)
tk.Button(root, text="=", width=4, height=2, command=calculate).grid(row=row_val, column=1, columnspan=3)

# Run the application
root.mainloop()
