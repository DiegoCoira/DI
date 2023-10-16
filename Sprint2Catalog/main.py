import tkinter as tk
from LoadingWindow import LoadingWindow  # Import the MainWindow class from the "window" module

# Check if this script is the main entry point
if __name__ == "__main__":
    root = tk.Tk()  # Create a tkinter main window
    app = LoadingWindow(root)  # Create an instance of the MainWindow class
    root.mainloop()