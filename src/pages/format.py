import tkinter as tk
from tkinter import ttk, scrolledtext
from ..formatting import NamingConventionFormatter
from ..constants import NAMING_CONVENTIONS
from ..component.notification import Notification

class FormatPage(ttk.Frame):
    def __init__(self, parent, language_manager):
        super().__init__(parent)
        self.language_manager = language_manager

        label = ttk.Label(self, text=self.language_manager.get_text("app_title"))
        label.pack(pady=10)

        # Input Text Area
        self.input_label = ttk.Label(self, text=self.language_manager.get_text("format"))
        self.input_label.pack(pady=5)

        self.input_text = scrolledtext.ScrolledText(self, width=30, height=5)
        self.input_text.pack(pady=5)

        # Naming Convention Selection using Buttons
        self.convention_label = ttk.Label(self, text=self.language_manager.get_text("actionSelectNamingConvention"))
        self.convention_label.pack(pady=5)

        self.selected_convention = None

        # Create buttons for each naming convention
        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.pack(pady=5)

        for convention in NAMING_CONVENTIONS:
            button_label = self.language_manager.get_text(convention)
            button = ttk.Button(self.buttons_frame, text=button_label, command=lambda c=convention: self.select_convention(c))
            button.pack(side=tk.LEFT, padx=2)

        # Output Text Area
        self.output_label = ttk.Label(self, text=self.language_manager.get_text("captionFormattedPreview"))
        self.output_label.pack(pady=5)

        self.output_text = scrolledtext.ScrolledText(self, width=30, height=5, state='disabled')
        self.output_text.pack(pady=5)

        # Initialize formatter
        self.formatter = NamingConventionFormatter()

        # Initialize Notification Component
        self.notification = Notification(self)

    def select_convention(self, convention):
        self.selected_convention = convention
        self.format_text()  # Automatically format on selection

    def format_text(self):
        input_text = self.input_text.get("1.0", tk.END).strip()
        convention = self.selected_convention
        formatted_text = ""

        # Check the selected naming convention
        if convention not in NAMING_CONVENTIONS:
            self.output_text.config(state='normal')
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, self.language_manager.get_text("msgInvalidInput"))
            self.output_text.config(state='disabled')
            return

        # Mapping conventions to their respective formatting methods
        convention_map = {
            "CAMEL_CASE": self.formatter.camel_case,
            "PASCAL_CASE": self.formatter.pascal_case,
            "SNAKE_CASE": self.formatter.snake_case,
            "KEBAB_CASE": self.formatter.kebab_case,
            "UPPER_CASE": self.formatter.upper_case,
            "HUNGARIAN_NOTATION": lambda text: self.formatter.hungarian_notation(text, "str"),  # Example prefix
            "FLAT_CASE": self.formatter.flat_case,
            "CONTEXTUAL_CASE": lambda text: self.formatter.contextual_naming(text, "get")  # Example action
        }

        # Get the appropriate formatting function from the map
        formatting_function = convention_map.get(convention)
        
        if formatting_function:
            formatted_text = formatting_function(input_text)

        self.output_text.config(state='normal')  # Enable editing
        self.output_text.delete("1.0", tk.END)  # Clear previous output
        self.output_text.insert(tk.END, formatted_text)  # Display formatted text
        self.output_text.config(state='disabled')  # Disable editing

        # Copy the formatted text to clipboard
        self.clipboard_clear()  # Clear current clipboard
        self.clipboard_append(formatted_text)  # Add formatted text to clipboard
        self.update()  # Ensure clipboard is updated

        # Show notification
        self.notification.show(self.language_manager.get_text("msgCopiedToClipboard"))