import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

from .language import LanguageManager
from .pages.home import HomePage
from .pages.format import FormatPage
from .pages.about import AboutPage
from .pages.moduleFormat import ModuleFunctionFormatPage
from .pages.entityGeneration import EntityClassGenerator

class App:
    def __init__(self, master):
        self.master = master
        self.style = Style()
        self.language_manager = LanguageManager()
        master.title(self.language_manager.get_text("app_title"))
        
        self.nav_frame = ttk.Frame(master)
        self.nav_frame.pack(side=tk.TOP, fill=tk.X)

        self.format_button = ttk.Button(self.nav_frame, text=self.language_manager.get_text("format"), command=self.show_format)
        self.format_button.pack(side=tk.LEFT)

        self.module_format_button = ttk.Button(self.nav_frame, text=self.language_manager.get_text("moduleFormat"), command=self.show_module_format)
        self.module_format_button.pack(side=tk.LEFT)

        self.entity_generation_button = ttk.Button(self.nav_frame, text=self.language_manager.get_text("captionEntityGeneration"), command=self.show_entity_generation)
        self.entity_generation_button.pack(side=tk.LEFT)

        self.about_button = ttk.Button(self.nav_frame, text=self.language_manager.get_text("about"), command=self.show_about)
        self.about_button.pack(side=tk.LEFT)

        self.language_button = ttk.Button(self.nav_frame, text="Switch to Chinese (Traditional)", command=self.switch_language)
        self.language_button.pack(side=tk.LEFT)

        self.content_frame = ttk.Frame(master)
        self.content_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.home_page = HomePage(self.content_frame, self.language_manager)
        self.format_page = FormatPage(self.content_frame, self.language_manager)
        self.module_format_page = ModuleFunctionFormatPage(self.content_frame, self.language_manager)
        self.entity_generation_page = EntityClassGenerator(self.content_frame, self.language_manager)
        self.about_page = AboutPage(self.content_frame, self.language_manager)

        self.show_format()

    def switch_language(self):
        new_lang = 'zh' if self.language_manager.current_language == 'en' else 'en'
        self.language_manager.switch_language(new_lang)
        self.update_texts()

    def update_texts(self):
        self.master.title(self.language_manager.get_text("app_title"))
        self.format_button.config(text=self.language_manager.get_text("format"))
        self.module_format_button.config(text=self.language_manager.get_text("format"))
        self.about_button.config(text=self.language_manager.get_text("about"))
        self.language_button.config(text=self.language_manager.get_text("actionSwitchEnglish") if self.language_manager.current_language == 'zh' else self.language_manager.get_text("actionSwitchChinese"))


    def show_format(self):
        self.module_format_page.pack_forget()
        self.about_page.pack_forget()
        self.entity_generation_page.pack_forget()
        self.format_page.pack(fill=tk.BOTH, expand=True)
    
    def show_module_format(self):
        self.format_page.pack_forget()
        self.about_page.pack_forget()
        self.entity_generation_page.pack_forget()
        self.module_format_page.pack(fill=tk.BOTH, expand=True)
    
    def show_entity_generation(self):
        self.format_page.pack_forget()
        self.module_format_page.pack_forget()
        self.about_page.pack_forget()
        self.entity_generation_page.pack(fill=tk.BOTH, expand=True)
    
    def show_about(self):
        self.format_page.pack_forget()
        self.module_format_page.pack_forget()
        self.entity_generation_page.pack_forget()
        self.about_page.pack(fill=tk.BOTH, expand=True)

def run_app():
    root = tk.Tk()
    root.geometry("600x400")  # Set fixed window size (width x height)
    app = App(root)
    root.mainloop()