from tkinter import ttk
import tkinter as tk
from cell import CatalogCell
from tkinter import messagebox
from PIL import Image, ImageTk

class MainWindow():

    def on_button_clicked(self, cell):
        message = "Has hecho click en la celda" + cell.title
        messagebox.showinfo("Informacion", message)

    def __init__(self,root):
        root.title("MainWindow")

        self.cells = [
            CatalogCell("BoyDinner", "catalog/data/unedited/BoyDinner.jpg"),
            CatalogCell("mi amigo dice", "catalog/data/unedited/mi amigo dice.jpg"),
            CatalogCell("Napoleon", "catalog/data/unedited/Napoleon.jpg"),
            CatalogCell("Tenemos", "catalog/data/unedited/Tenemos.png"),
            CatalogCell("We love we live we", "catalog/data/unedited/We love we live we.jpg")
        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image= cell.image_tk, text=cell.title, compound= tk.BOTTOM)
            label.grid(row=i,column=0)
            label.bind("<Button-1>", lambda event, celda = cell: self.on_button_clicked(celda))
    