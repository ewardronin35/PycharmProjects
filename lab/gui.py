import tkinter as tk

class ClickCounterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Click Counter")

        self.count = 0

        self.label = tk.Label(master, text="Click the button to count:")
        self.label.pack()

        self.button = tk.Button(master, text="Click me!", command=self.increment_count)
        self.button.pack()

        self.count_label = tk.Label(master, text="Count: 0")
        self.count_label.pack()

    def increment_count(self):
        self.count += 1
        self.count_label.config(text="Count: {}".format(self.count))

root = tk.Tk()
click_counter = ClickCounterGUI(root)
root.mainloop()