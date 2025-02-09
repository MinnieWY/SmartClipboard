import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk

class AboutPage(ttk.Frame):
    def __init__(self, parent, language_manager):
        super().__init__(parent)
        self.language_manager = language_manager

        # Title Label
        self.title_label = ttk.Label(self, text=self.language_manager.get_text("about"), font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        # Description Label
        self.description_label = ttk.Label(self, text=self.language_manager.get_text("about_description"), wraplength=400)
        self.description_label.pack(pady=5)

        # Load an icon image
        self.icon_image = Image.open("src/icons/github-brands-solid-png.png")
        desired_size = (50, 50) 
        self.icon_image = self.icon_image.resize(desired_size, Image.ANTIALIAS)
        self.icon = ImageTk.PhotoImage(self.icon_image)

        # GitHub Link Button
        self.github_link = ttk.Button(self, image=self.icon, text=self.language_manager.get_text("github_link"), command=self.open_github)
        self.github_link.pack(pady=10)

    def open_github(self):
        webbrowser.open("https://github.com/MinnieWY/SmartClipboard")

    def update_texts(self):
        self.title_label.config(text=self.language_manager.get_text("about"))
        self.description_label.config(text=self.language_manager.get_text("about_description"))
        self.github_link.config(text=self.language_manager.get_text("github_link"))