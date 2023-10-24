from window import MainWindow  # Import the MainWindow class from the "window" module
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from LoadingWindow import LoadingWindow


def launch_main_window(json_data):
    root = tk.Tk()
    app = MainWindow(root, json_data)
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoadingWindow(root)
    root.mainloop()