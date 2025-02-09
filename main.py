import tkinter as tk
import pyperclip

def copy_text():
    text = input_field.get()
    pyperclip.copy(text)

app = tk.Tk()
app.title("Clipboard App")

input_field = tk.Entry(app)
input_field.pack()

copy_button = tk.Button(app, text="Copy", command=copy_text)
copy_button.pack()

app.mainloop()