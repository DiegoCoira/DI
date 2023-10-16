import tkinter as tk
import threading
import json  # Import the json module for working with JSON data
from PIL import Image, ImageTk

class LoadingWindow:
    def __init__(self, root):
        root.title("LoadingWindow")
        self.root = root
        self.root.title ("Cargando...")
        self.root.geometry("170x120")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        self.label.pack(side=tk.TOP, pady=18)

        label_bg_color = self.label.cget("bg")

        self.canvas = tk.Canvas(self.root,width=60, height=60,bg=label_bg_color)
        self.canvas.pack()

        self.progress = 0

        self.draw_progress_circle(self.progress)

        self.update_progress_circle()

        self.thread = threading.Thread(target= self.fetch_json_data)
        self.thread.start()


    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")
        angle = int(360 * (progress / 100))

        self.canvas.create_arc(10, 10, 40, 40, start=0, extent=angle, tags="progress", outline="green", width=4, style=tk.ARC)


    def update_progress_circle(self):
        if self.progress < 100:
            self.progress += 1
        else:
            self.progress = 0

        self.draw_progress_circle(self.progress)
        self.root.after(5, self.update_progress_circle)



    def fetch_json_data(self):
        # Replace the file path with the actual path to your JSON file
        file_path = "C:\\Users\\Alumno\\Desktop\\Desarrollo de interfaces\\DI\\Sprint2Catalog\\catalog.json"

        try:
            with open(file_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)

                # Process the JSON data
                for item in data:
                    name = item.get("name")
                    description = item.get("description")
                    image_url = item.get("image_url")
                    # You can add code to display the data in your Tkinter window

        except FileNotFoundError as e:
            print("File not found:", e)
       