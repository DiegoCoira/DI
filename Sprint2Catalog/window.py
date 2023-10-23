# Import necessary modules and classes from tkinter, PIL, and your custom modules
from tkinter import ttk
import tkinter as tk
from cell import CatalogCell
from tkinter import messagebox
from PIL import Image, ImageTk
from detail_window import DetailWindow

# Define a class called MainWindow
class MainWindow():

    # Define a method to handle button click events
    def on_button_clicked(self, cell):
        # Create a DetailWindow instance to display details of the clicked cell
        detail_window = DetailWindow(self.root, cell.title, cell.image_tk, cell.description)

    # Constructor method for the MainWindow class
    def __init__(self, root):
        # Set the window title
        root.title("MainWindow")
        self.root = root  # Store a reference to the main window

        # Create a list of CatalogCell instances
        self.cells = [
            CatalogCell("BoyDinner", "catalog/data/unedited/BoyDinner.jpg",
                        "Average boy dinner, watching Sam Sulek and having an awesome dinner"),
            CatalogCell("mi amigo dice", "catalog/data/unedited/mi amigo dice.jpg",
                        "Mi amigo dice meme, incredible meme (never saw it in my life, found it on Google)"),
            CatalogCell("Napoleon", "catalog/data/unedited/Napoleon.jpg",
                        "There's nothing we can do, Napoleon meme shows up 32410253 times on Tiktok"),
            CatalogCell("Tenemos", "catalog/data/unedited/Tenemos.png",
                        "Typical communist meme, quite funny and it's all over Tiktok"),
            CatalogCell("We love we live we", "catalog/data/unedited/We love we live we.jpg",
                        "My buddy шайлушай, a tiresome meme that shows up 20419439 times")
        ]

        # Create labels with images and titles for each cell and bind a click event to each label
        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)  # Place the label in the window
            # Bind a left-click event to the label and pass the corresponding cell to the event handler
            label.bind("<Button-1>", lambda event, celda=cell: self.on_button_clicked(celda))
