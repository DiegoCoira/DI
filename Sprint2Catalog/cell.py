from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Define a class for a catalog cell
class CatalogCell:
    def __init__(self, name, descripcion, image_url, imagen):
        self.name = name
        self.descripcion = descripcion
        self.image_url = image_url
        self.imagen = imagen   