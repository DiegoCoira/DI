from window import MainWindow  # Import the MainWindow class from the "window" module
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from LoadingWindow import LoadingWindow

# Check if this script is the main entry point
def launch_main_window(json_data):
    root = tk()
    app = MainWindow(root, json_data)
    root.mainloop()

if __name__ == "__main__":
    root = tk()
    app = LoadingWindow(root)
    root.mainloop()
    if app.data_ready.is_set():  # Verifica si los datos están listos
        launch_main_window(app.json_data)