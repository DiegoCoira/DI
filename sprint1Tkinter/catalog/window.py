from tkinter import ttk
import tkinter as tk
from cell import CatalogCell
from tkinter import messagebox
from PIL import Image, ImageTk
from detail_window import DetailWindow

class MainWindow():

    def on_button_clicked(self, cell):
        detail_window = DetailWindow(self.root, cell.title, cell.image_tk, cell.description)


    def __init__(self,root):
        root.title("MainWindow")
        self.root = root 

        self.cells = [
            CatalogCell("BoyDinner", "catalog/data/unedited/BoyDinner.jpg","Average boy dinner, whatching Sam Sulek and having an awesome dinner"),
            CatalogCell("mi amigo dice", "catalog/data/unedited/mi amigo dice.jpg", "Mi amigo dice meme, increible meme (no o vin na miña vida, encontreino en google)"),
            CatalogCell("Napoleon", "catalog/data/unedited/Napoleon.jpg","No hay nada que podamos hacer, meme de napoleon saleume 32410253 veces en Tiktok"),
            CatalogCell("Tenemos", "catalog/data/unedited/Tenemos.png", "Tipico meme comunista, bastante gracioso con utilida e saleume en tiktok"),
            CatalogCell("We love we live we", "catalog/data/unedited/We love we live we.jpg", "Mi compa el шайлушай, meme cansino saleu 20419439  veces")
        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image= cell.image_tk, text=cell.title, compound= tk.BOTTOM)
            label.grid(row=i,column=0)
            label.bind("<Button-1>", lambda event, celda = cell: self.on_button_clicked(celda))
    