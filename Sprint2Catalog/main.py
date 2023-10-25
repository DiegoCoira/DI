# Import necessary modules and classes
from window import MainWindow  # Import the MainWindow class from the "window" module
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from LoadingWindow import LoadingWindow

# Define a function to launch the main window with JSON data
def launch_main_window(json_data):
    # Create a Tkinter root window
    root = tk.Tk()
    
    # Initialize the main application window with the JSON data
    app = MainWindow(root, json_data)
    
    # Start the main event loop to run the application
    root.mainloop()

# Check if this script is the main module (not imported)
if __name__ == "__main__":
    # Create a Tkinter root window
    root = tk.Tk()
    
    # Initialize the LoadingWindow to display a loading screen
    app = LoadingWindow(root)
    
    # Start the main event loop to show the loading screen
    root.mainloop()
