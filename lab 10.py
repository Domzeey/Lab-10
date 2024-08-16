#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 21:16:10 2024

@author: dominion
"""

import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Create input frame
        input_frame = tk.Frame(root)
        input_frame.pack()

        # Create labels and entry widgets for input numbers
        tk.Label(input_frame, text="Enter Number 1:").pack(side=tk.LEFT)
        self.num1_entry = tk.Entry(input_frame)
        self.num1_entry.pack(side=tk.LEFT)
        
        tk.Label(input_frame, text="Enter Number 2:").pack(side=tk.LEFT)
        self.num2_entry = tk.Entry(input_frame)
        self.num2_entry.pack(side=tk.LEFT)

        # Create radio buttons for selecting operation
        operation_frame = tk.Frame(root)
        operation_frame.pack()
        
        self.operation = tk.IntVar()
        self.operation.set(1)  # Default to addition
        
        tk.Label(operation_frame, text="Select Operation:").pack(side=tk.LEFT)
        tk.Radiobutton(operation_frame, text="Addition", variable=self.operation, value=1).pack(side=tk.LEFT)
        tk.Radiobutton(operation_frame, text="Subtraction", variable=self.operation, value=2).pack(side=tk.LEFT)
        tk.Radiobutton(operation_frame, text="Multiplication", variable=self.operation, value=3).pack(side=tk.LEFT)
        tk.Radiobutton(operation_frame, text="Division", variable=self.operation, value=4).pack(side=tk.LEFT)
        tk.Radiobutton(operation_frame, text="Remainder", variable=self.operation, value=5).pack(side=tk.LEFT)
        tk.Radiobutton(operation_frame, text="Exponent", variable=self.operation, value=6).pack(side=tk.LEFT)

        # Create a button to perform the calculation
        calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        calculate_button.pack()

        # Create a label to display the result
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation.get()

            if operation == 1:
                result = num1 + num2
            elif operation == 2:
                result = num1 - num2
            elif operation == 3:
                result = num1 * num2
            elif operation == 4:
                result = num1 / num2
            elif operation == 5:
                result = num1 % num2
            elif operation == 6:
                result = num1 ** num2
            else:
                result = "Invalid operation"

            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()