import tkinter as tk
from tkinter import ttk
from ..text_manager import copy_text, paste_text, clear_text, update_readonly_area

class HomePage(ttk.Frame):
    def __init__(self, parent, language_manager):
        super().__init__(parent)
        self.language_manager = language_manager
        
        self.input_area = tk.Text(self, wrap='word', height=15, width=40)
        self.input_area.pack(side=tk.LEFT, padx=5, pady=5)

        self.readonly_area = tk.Text(self, wrap='word', height=15, width=40, state=tk.DISABLED)
        self.readonly_area.pack(side=tk.RIGHT, padx=5, pady=5)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=5)

        copy_button = ttk.Button(button_frame, text=self.language_manager.get_text("copy"), command=self.copy_text)
        copy_button.pack(side=tk.LEFT, padx=5)

        paste_button = ttk.Button(button_frame, text=self.language_manager.get_text("paste"), command=self.paste_text)
        paste_button.pack(side=tk.LEFT, padx=5)

        clear_button = ttk.Button(button_frame, text=self.language_manager.get_text("clear"), command=self.clear_text)
        clear_button.pack(side=tk.LEFT, padx=5)

        self.update_texts()  # Initial text update

    def copy_text(self):
        copy_text(self.input_area, self.readonly_area)

    def paste_text(self):
        paste_text(self.input_area, self.readonly_area)

    def clear_text(self):
        clear_text(self.input_area, self.readonly_area)

    def update_texts(self):
        # Update text dynamically
        pass  # Implement additional text updates if necessary