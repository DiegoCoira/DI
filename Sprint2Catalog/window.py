# Import necessary modules and classes from tkinter, PIL, and your custom modules
from io import BytesIO
from tkinter import Label, ttk
import tkinter as tk
from cell import CatalogCell
from tkinter import messagebox
from PIL import Image, ImageTk
from detail_window import DetailWindow
import requests

# Define a class called MainWindow
class MainWindow():
    
    def load_image_from_url(self, url):
      response = requests.get(url)
      img_data = Image.open(BytesIO(response.content))
      img = ImageTk.PhotoImage((img_data).resize((250, 250), Image.Resampling.LANCZOS))
      return img

    def on_button_clicked(self, cell):
        detail_window = DetailWindow(cell)

    
    def __init__(self, root, json_data):
        root.title("MainWindow")
        self.root = root

        self.cell_frame = tk.Frame(self.root)
        self.cell_frame.grid(row=0, column=0, padx=10, pady=10)

        self.cell_list = [] 
        for i, data in enumerate(json_data):
            name = data["name"] 
            descripcion = data["description"]
            url = data["image_url"]
            imagen = self.load_image_from_url(url)

            cell = CatalogCell(name, descripcion, url, imagen) 
            self.cell_list.append(cell)

            label = Label(self.cell_frame, image=cell.imagen, text=name, compound=tk.BOTTOM)
            label.grid(row=i, column=0, sticky="nsew")
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))

        for i in range(len(self.cell_list)):
            self.cell_frame.grid_rowconfigure(i, weight=1)
