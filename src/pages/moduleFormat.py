import tkinter as tk
from tkinter import ttk
import pyperclip  # Import the pyperclip module for clipboard functionality
from ..formatting import NamingConventionFormatter
from ..component.notification import Notification

class ModuleFunctionFormatPage(ttk.Frame):
    def __init__(self, parent, language_manager):
        super().__init__(parent)
        self.language_manager = language_manager

        # Frame for input fields
        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(pady=5)

        # Module Name Input
        self.module_label = ttk.Label(self.input_frame, text=self.language_manager.get_text("captionModuleName"))
        self.module_label.pack(side=tk.LEFT)

        self.module_entry = ttk.Entry(self.input_frame, width=20)
        self.module_entry.pack(side=tk.LEFT, padx=5)

        # Function Name Input
        self.function_label = ttk.Label(self.input_frame, text=self.language_manager.get_text("captionFunctionName"))
        self.function_label.pack(side=tk.LEFT)

        self.function_entry = ttk.Entry(self.input_frame, width=20)
        self.function_entry.pack(side=tk.LEFT, padx=5)

        # Format Button
        self.format_button = ttk.Button(self, text=self.language_manager.get_text("format"), command=self.format_names)
        self.format_button.pack(pady=10)

        # Output Frame for formatted results
        self.output_frame = ttk.Frame(self)
        self.output_frame.pack(pady=5)

        # Initialize formatter
        self.formatter = NamingConventionFormatter()

        # Initialize Notification Component
        self.notification = Notification(self)

    def format_names(self):
        module_name = self.module_entry.get().strip()
        function_name = self.function_entry.get().strip()

        # Validate input
        if not module_name or not function_name:
            self.notification.show(self.language_manager.get_text("msgInputRequired"), "error")
            return

        # Clear previous results
        for widget in self.output_frame.winfo_children():
            widget.destroy()

        # Example formatting results
        formatted_results = {
            "Container": self.formatter.format_frontend_container(module_name, function_name),
            "Component": self.formatter.format_frontend_component(module_name, function_name),
            "Reducer": self.formatter.format_frontend_reducer(module_name, function_name),
            "Saga": self.formatter.format_frontend_saga(module_name),
            "Controller": self.formatter.format_backend_rest_controller(module_name),
            "Service": self.formatter.format_backend_service(module_name),
            "Service Implementation": self.formatter.format_backend_service_implement(module_name),
        }

        # Create table headers
        ttk.Label(self.output_frame, text="Description", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.output_frame, text="Formatted Result", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(self.output_frame, text="", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=5, pady=5)  # Empty column for spacing

        # Display formatted results in table format
        for row_index, (label, formatted) in enumerate(formatted_results.items(), start=1):
            # Description
            description_label = ttk.Label(self.output_frame, text=label)
            description_label.grid(row=row_index, column=0, sticky='w', padx=5, pady=2)

            # Formatted result
            result_label = ttk.Label(self.output_frame, text=formatted, wraplength=300)
            result_label.grid(row=row_index, column=1, sticky='w', padx=5, pady=2)

            # Copy button
            copy_button = ttk.Button(self.output_frame, text="Copy", command=lambda text=formatted: self.copy_to_clipboard(text))
            copy_button.grid(row=row_index, column=2, padx=5, pady=2)

    def copy_to_clipboard(self, text):
        """Copy the given text to the clipboard."""
        pyperclip.copy(text)
        self.notification.show(self.language_manager.get_text("msgCopiedToClipboard"), "success")