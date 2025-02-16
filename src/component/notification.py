import tkinter as tk
from tkinter import ttk

class Notification(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = ttk.Label(self, text="", foreground="green")
        self.label.pack(pady=5)
        self.pack()

    def show(self, message):
        self.label.config(text=message)
        self.after(3000, self.clear)  # Clear after 3 seconds

    def clear(self):
        self.label.config(text="")