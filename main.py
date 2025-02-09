import tkinter as tk
from ttkbootstrap import Style
import pyperclip

# Initialize the style
style = Style()

def copy_text():
    text = input_field.get()
    pyperclip.copy(text)

def paste_text():
    text = pyperclip.paste()
    input_field.delete(0, tk.END)
    input_field.insert(0, text)

# Create the main application window
app = style.master
app.title("Clipboard App")

# Create and place widgets
input_field = style.Entry(app)
input_field.pack(pady=10)

copy_button = style.Button(app, text="Copy", command=copy_text)
copy_button.pack(pady=5)

paste_button = style.Button(app, text="Paste", command=paste_text)
paste_button.pack(pady=5)

# Run the application
app.mainloop()