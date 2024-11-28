import tkinter as tk
from tkinter import messagebox
from converters.length_converter import convert_length
from converters.weight_converter import convert_weight
from converters.temperature_converter import convert_temperature
from utils.input_validation import validate_input

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")

        # Set the window size
        self.root.geometry("400x400")

        # Create dropdown for selecting unit type
        self.unit_type_label = tk.Label(root, text="Select Unit Type")
        self.unit_type_label.pack()

        self.unit_type = tk.StringVar()
        self.unit_type_dropdown = tk.OptionMenu(root, self.unit_type, "Length", "Weight", "Temperature")
        self.unit_type.set("Length")  # default value
        self.unit_type_dropdown.pack()

        # Create input fields
        self.value_label = tk.Label(root, text="Enter Value:")
        self.value_label.pack()

        self.value_entry = tk.Entry(root)
        self.value_entry.pack()

        self.result_label = tk.Label(root, text="Converted Value:")
        self.result_label.pack()

        self.result_var = tk.StringVar()
        self.result_label_value = tk.Label(root, textvariable=self.result_var)
        self.result_label_value.pack()

        # Create convert button
        self.convert_button = tk.Button(root, text="Convert", command=self.convert)
        self.convert_button.pack()

    def convert(self):
        # Get user input
        value = self.value_entry.get()
        unit_type = self.unit_type.get()

        # Validate input
        if not validate_input(value):
            messagebox.showerror("Input Error", "Please enter a valid number.")
            return

        value = float(value)

        # Perform conversion based on selected unit type
        if unit_type == "Length":
            result = convert_length(value)
        elif unit_type == "Weight":
            result = convert_weight(value)
        elif unit_type == "Temperature":
            result = convert_temperature(value)

        # Display result
        self.result_var.set(f"{result} {unit_type.lower()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()
