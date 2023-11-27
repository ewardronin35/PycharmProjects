import tkinter as tk
from tkinter import messagebox

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Check if the username and password are correct (you can replace this with your authentication logic)
    if entered_username == "user" and entered_password == "password":
        messagebox.showinfo("Login Successful", "Welcome, {}!".format(entered_username))
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")


# Create and place username label and entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

password_entry = tk.Entry(root, show="*")  # show="*" to hide the password
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
