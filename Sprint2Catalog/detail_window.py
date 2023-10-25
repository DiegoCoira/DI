import tkinter as tk
from tkinter import Label, ttk

# Define a function to create a detail window for a CatalogCell object
def DetailWindow(cell):
    # Create a new top-level window (a pop-up window)
    root = tk.Toplevel()

    # Set the title of the detail window to the name of the CatalogCell                   
    root.title(cell.name) 
    
    # Center the detail window on the screen
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry(f"+{int(x)}+{int(y)}")
    

    # Create a label with the name of the CatalogCell and display it
    label1 = ttk.Label(root, text=cell.name) 
    label1.pack()

    # Create a label with the image (thumbnail) of the CatalogCell and display it
    label = ttk.Label(root, image=cell.imagen, compound=tk.BOTTOM) 
    label.pack()

     # Create a label with the description of the CatalogCell and display it
    label2 = ttk.Label(root, text=cell.descripcion) 
    label2.pack()
    
    # Start the main event loop for the detail window to handle user interactions
    root.mainloop()
        