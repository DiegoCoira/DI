# Import necessary modules
import tkinter as tk
import threading
from PIL import Image, ImageTk
import requests
from window import MainWindow

# Define a class for the loading window
class LoadingWindow:
    def __init__(self, root):
        self.finished = False  # A flag to track if the data loading is complete
        self.json_data = []    # Placeholder for JSON data

        self.root = root
        self.root.title("Cargando...")  # Set the title of the loading window

        # Center the loading window on the screen
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.geometry(f"+{int(x)}+{int(y)}")

        # Create a label to display a loading message
        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        self.label.pack(side=tk.TOP, pady=18)

        label_bg_color = self.label.cget("bg")

        # Create a canvas to draw a progress circle
        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()

        self.progress = 0  # Progress percentage

        self.draw_progress_circle(self.progress)

        # Update the progress circle
        self.update_progress_circle()

        # Start a separate thread to fetch JSON data
        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()

        # Check the status of the loading thread
        self.check_thread()

    def draw_progress_circle(self, progress):
        # Clear any previous drawings and draw a progress circle
        self.canvas.delete("progress")
        angle = int(360 * (progress / 100))
        self.canvas.create_arc(10, 10, 40, 40, start=0, extent=angle, tags="progress", outline="green", width=4, style=tk.ARC)

    def update_progress_circle(self):
        # Update the progress circle
        if self.progress < 100:
            self.progress += 1
        else:
            self.progress = 0

        self.draw_progress_circle(self.progress)
        self.root.after(4, self.update_progress_circle)

    def fetch_json_data(self):
        # Fetch JSON data from a URL
        response = requests.get("https://raw.githubusercontent.com/DiegoCoira/DI/main/Sprint2ApiRest/catalog.json")
        if response.status_code == 200:
            self.json_data = response.json()
            self.finished = True  # Set the finished flag when data is loaded

    def check_thread(self):
        # Check the status of the loading thread
        if self.finished:
            self.root.destroy()  # Close the loading window
            launch_main_window(self.json_data)  # Launch the main window with the JSON data
        else:
            self.root.after(100, self.check_thread)  # Check again after a delay

# Define a function to launch the main window with JSON data
def launch_main_window(json_data):
    root = tk.Tk()
    app = MainWindow(root, json_data)
    root.mainloop()
