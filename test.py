import pyperclip
import tkinter as tk

root = tk.Tk()
root.title("Clipboard Test")
root.geometry("200x100")

def copy_text():
    pyperclip.copy("Hello, Clipboard!")

button = tk.Button(root, text="Copy to Clipboard", command=copy_text)
button.pack(pady=20)

root.mainloop()