from tkinter import ttk
import tkinter as tk
from cell import CatalogCell
from tkinter import messagebox

class MainWindow():

    def on_button_clicked(self, cell):
        message = "Has hecho click en la celda" + cell.title
        messagebox.showinfo("Informacion", message)

    def __init__(self,root):
        root.title("MainWindow")

        self.cells = [
            CatalogCell("BoyDinner", "catalog/data/edited/BoyDinner.jpg"),
            CatalogCell("mi amigo dice", "catalog/data/edited/mi amigo dice.jpg"),
            CatalogCell("Napoleon", "catalog/data/edited/Napoleon.jpg"),
            CatalogCell("Tenemos", "catalog/data/edited/Tenemos.jpg"),
            CatalogCell("We love we live we", "catalog/data/edited/We love we live we.jpg")
        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image= cell.image_tk, text=cell.title, compound= tk.BOTTOM)
            label.grid(row=i,column=0)
            label.bind("<Button-1>", lambda event, celda = cell: self.on_button_clicked(celda))
    