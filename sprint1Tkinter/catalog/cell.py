from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class CatalogCell:
    def __init__(self, title, path, description):
        self.title = title
        self.path = path
        self.description = description

        image = Image.open(self.path)
        image = image.resize((150, 150), Image.LANCZOS) 
        self.image_tk = ImageTk.PhotoImage(image)