import tkinter as tk
from tkinter import ttk
import pyperclip  # Import the pyperclip module for clipboard functionality
from ..component.notification import Notification

class EntityClassGenerator(ttk.Frame):
    def __init__(self, parent, language_manager):
        super().__init__(parent)
        self.language_manager = language_manager

        # Frame for input fields
        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(pady=5)

        # Text area for pasted input
        self.input_text = tk.Text(self.input_frame, height=10, width=50)
        self.input_text.pack(pady=5)

        # Parse Button
        self.parse_button = ttk.Button(self.input_frame, text="Parse Input", command=self.parse_input)
        self.parse_button.pack(pady=5)

        # Generate Button
        self.generate_button = ttk.Button(self, text="Generate Entity Class", command=self.generate_entity_class)
        self.generate_button.pack(pady=10)

        # Output Frame for generated results with scrollbar
        self.output_frame = ttk.Frame(self)
        self.output_frame.pack(pady=5, fill=tk.BOTH, expand=True)

        # Create a canvas for scrolling
        self.canvas = tk.Canvas(self.output_frame)
        self.scrollbar = ttk.Scrollbar(self.output_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Initialize Notification Component
        self.notification = Notification(self)

    def parse_input(self):
        # Clear previous input fields
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Get the input text
        raw_input = self.input_text.get("1.0", tk.END).strip()

        # Initialize properties list
        properties = []

        # Split the input into lines and parse
        for line in raw_input.splitlines():
            parts = line.split()
            # Check if there are exactly two parts: column name and data type
            if len(parts) == 2:
                column_name, column_type = parts
                properties.append((column_name.strip(), column_type.strip()))
            else:
                # Handle cases with values like "NUMBER(19,0)"
                if len(parts) == 1:
                    column_name = parts[0].strip()
                    properties.append((column_name, "Object"))  # Default type if only column name is provided

        # Populate the fields with parsed data
        self.fields = []
        for column_name, column_type in properties:
            self.add_input_field(column_name, column_type)

        if not properties:
            self.notification.show("No valid properties found in the input.", "error")

    def add_input_field(self, column_name="", column_type=""):
        # Create a frame for the new input field
        field_frame = ttk.Frame(self.scrollable_frame)
        field_frame.pack(pady=2)

        # Column Name Input
        column_entry = ttk.Entry(field_frame, width=20)
        column_entry.pack(side=tk.LEFT, padx=5)
        column_entry.insert(0, column_name or self.language_manager.get_text("captionColumnName"))

        # Column Type Input
        type_entry = ttk.Entry(field_frame, width=10)
        type_entry.pack(side=tk.LEFT, padx=5)
        type_entry.insert(0, column_type or self.language_manager.get_text("captionColumnType"))

        # Add the entries to the fields list
        self.fields.append((column_entry, type_entry))

        # Remove Button
        remove_button = ttk.Button(field_frame, text="Remove", command=lambda: self.remove_input_field(field_frame))
        remove_button.pack(side=tk.LEFT, padx=5)

    def remove_input_field(self, field_frame):
        # Remove the specified input field frame
        field_frame.destroy()
        self.fields = [field for field in self.fields if field[0].winfo_parent() != field_frame]

    def generate_entity_class(self):
        # Collect column names and types
        properties = []
        for column_entry, type_entry in self.fields:
            column_name = column_entry.get().strip()
            column_type = type_entry.get().strip()
            if column_name and column_type:
                properties.append((column_name, column_type))

        # Validate input
        if not properties:
            self.notification.show(self.language_manager.get_text("captionColumnType"), "error")
            return

        # Clear previous results
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Generate entity class code
        entity_code_lines = ["public class Entity {"]  # Start of the class
        for column_name, column_type in properties:
            property_name = self.convert_to_property_name(column_name)
            entity_code_lines.append(f"    private {self.map_to_java_type(column_type)} {property_name};")

        entity_code_lines.append("}")  # End of the class
        entity_code = "\n".join(entity_code_lines)

        # Display generated code
        result_label = ttk.Label(self.scrollable_frame, text=entity_code, wraplength=300)
        result_label.pack(pady=2)

        # Copy button
        copy_button = ttk.Button(self.scrollable_frame, text="Copy", command=lambda: self.copy_to_clipboard(entity_code))
        copy_button.pack(pady=2)

    def convert_to_property_name(self, column_name):
        # Convert snake_case to camelCase
        parts = column_name.split('_')
        return parts[0] + ''.join(part.capitalize() for part in parts[1:])

    def map_to_java_type(self, db_type):
        # Map database types to Java types
        type_mapping = {
            "VARCHAR2": "String",
            "NUMBER": "Long",  # Adjusted to handle NUMBER types generally
            # Add more mappings as needed
        }
        return type_mapping.get(db_type.split('(')[0].upper(), "Object")  # Default to Object if type not found

    def copy_to_clipboard(self, text):
        """Copy the given text to the clipboard."""
        pyperclip.copy(text)
        self.notification.show(self.language_manager.get_text("msgCopiedToClipboard"), "success")