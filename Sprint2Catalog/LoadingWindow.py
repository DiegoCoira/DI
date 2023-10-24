import tkinter as tk
import threading
from PIL import Image, ImageTk
import requests
from window import MainWindow

class LoadingWindow:
    def __init__(self, root):
    
        self.finished = False
        self.json_data = []

        self.root = root
        self.root.title ("Cargando...")
        
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.geometry(f"+{int(x)}+{int(y)}")

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
        self.check_thread()


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
        self.root.after(4, self.update_progress_circle)

    def fetch_json_data(self):
        response = requests.get("https://raw.githubusercontent.com/DiegoCoira/DI/main/Sprint2ApiRest/catalog.json")
        if response.status_code == 200:
            self.json_data = response.json()
            self.finished = True

    def check_thread(self):
        if self.finished:
            self.root.destroy()
            launch_main_window(self.json_data)
        else:
            self.root.after(100, self.check_thread)


def launch_main_window(json_data):
    root = tk.Tk()
    app = MainWindow(root,json_data)
    root.mainloop()
