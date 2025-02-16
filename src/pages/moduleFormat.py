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
            "container": self.formatter.format_frontend_container(module_name, function_name),
            "component": self.formatter.format_frontend_component(module_name, function_name),
            "reducer": self.formatter.format_frontend_reducer(module_name, function_name),
            "saga": self.formatter.format_frontend_saga(module_name),
            "controller": self.formatter.format_backend_rest_controller(module_name),
            "service": self.formatter.format_backend_service(module_name),
            "serviceImpl": self.formatter.format_backend_service_implement(module_name),
        }

        # Display formatted results with copy buttons
        for label, formatted in formatted_results.items():
            caption_label = "caption" + self.formatter.pascal_case(label)
            label_string = self.language_manager.get_text(caption_label)

            # Create a frame for each result
            result_frame = ttk.Frame(self.output_frame)
            result_frame.pack(pady=2)

            # Label for the formatted result with left alignment
            result_label = ttk.Label(result_frame, text=f"{label_string}: {formatted}", wraplength=300, anchor='w')
            result_label.grid(row=0, column=0, sticky='w')

            # Copy button
            copy_button = ttk.Button(result_frame, text="Copy", command=lambda text=formatted: self.copy_to_clipboard(text))
            copy_button.grid(row=0, column=1, padx=5)

    def copy_to_clipboard(self, text):
        """Copy the given text to the clipboard."""
        pyperclip.copy(text)
        self.notification.show(self.language_manager.get_text("msgCopiedToClipboard"), "success")