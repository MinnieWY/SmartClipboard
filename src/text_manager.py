import pyperclip

def copy_text(input_area, readonly_area):
    text = input_area.get("1.0", "end-1c").strip()
    pyperclip.copy(text)
    update_readonly_area(input_area, readonly_area)

def paste_text(input_area, readonly_area):
    text = pyperclip.paste()
    input_area.delete("1.0", "end")
    input_area.insert("end", text)
    update_readonly_area(input_area, readonly_area)

def clear_text(input_area, readonly_area):
    input_area.delete("1.0", "end")
    readonly_area.config(state="normal")
    readonly_area.delete("1.0", "end")
    readonly_area.config(state="disabled")

def update_readonly_area(input_area, readonly_area):
    text = input_area.get("1.0", "end-1c").strip()
    readonly_area.config(state="normal")
    readonly_area.delete("1.0", "end")
    readonly_area.insert("end", text)
    readonly_area.config(state="disabled")