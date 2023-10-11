import tkinter as tk
from tkinter import ttk

# Define a class for the DetailWindow
class DetailWindow:
    def __init__(self, root, title, image, description):
        self.root = root
        self.title = title
        self.image = image
        self.description = description

        # Create a new pop up window for displaying all the details
        self.window = tk.Toplevel(root)
        self.window.title(self.title)  # Set the title of the window 

        # To display the image
        image_label = ttk.Label(self.window, image=self.image)
        image_label.pack()

        # To display the title with a specified font size
        title_label = ttk.Label(self.window, text=self.title, font=("Roboto", 16))
        title_label.pack()

        # To display the description with text wrapping
        description_label = ttk.Label(self.window, text=self.description, wraplength=300)
        description_label.pack()
