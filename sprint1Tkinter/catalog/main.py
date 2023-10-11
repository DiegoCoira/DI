from window import MainWindow  # Import the MainWindow class from the "window" module
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Check if this script is the main entry point
if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()  # Create a tkinter main window
    app = MainWindow(root)  # Create an instance of the MainWindow class
    root.mainloop()  # Start the tkinter main event loop to run the application
