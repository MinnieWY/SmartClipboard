import tkinter as tk
from tkinter import ttk, scrolledtext
from ..formatting import NamingConventionFormatter
from ..constants import NAMING_CONVENTIONS

class FormatPage(ttk.Frame):
    def __init__(self, parent, language_manager):
        super().__init__(parent)
        self.language_manager = language_manager
        
        label = ttk.Label(self, text="Text Formatting")
        label.pack(pady=10)

        # Input Text Area
        self.input_label = ttk.Label(self, text=self.language_manager.get_text("format"))
        self.input_label.pack(pady=5)

        self.input_text = scrolledtext.ScrolledText(self, width=30, height=5)
        self.input_text.pack(pady=5)

        # Naming Convention Selection
        self.convention_label = ttk.Label(self, text=self.language_manager.get_text("actionSelectNamingConvention"))
        self.convention_label.pack(pady=5)

        self.convention_var = tk.StringVar()
        self.convention_combo = ttk.Combobox(self, textvariable=self.convention_var, values=NAMING_CONVENTIONS)
        self.convention_combo.pack(pady=5)
        self.convention_combo.current(0)  # Default to the first option

        # Format Button
        self.format_button = ttk.Button(self, text="Format", command=self.format_text)
        self.format_button.pack(pady=10)

        # Output Text Area
        self.output_label = ttk.Label(self, text=self.language_manager.get_text("captionFormattedPreview"))
        self.output_label.pack(pady=5)

        self.output_text = scrolledtext.ScrolledText(self, width=30, height=5)
        self.output_text.pack(pady=5)

        # Initialize formatter
        self.formatter = NamingConventionFormatter()

    def format_text(self):
        input_text = self.input_text.get("1.0", tk.END).strip()
        convention = self.convention_var.get()
        formatted_text = ""

        # Check the selected naming convention using the constant
        if convention not in NAMING_CONVENTIONS:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, self.language_manager.get_text("msgInvalidInput"))
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

        self.output_text.delete("1.0", tk.END)  # Clear previous output
        self.output_text.insert(tk.END, formatted_text)  # Display formatted text