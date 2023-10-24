import tkinter as tk
from tkinter import Label, ttk

def DetailWindow(cell):
    root = tk.Toplevel()
                         
    root.title(cell.name) 
    
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry(f"+{int(x)}+{int(y)}")
    
    label1 = ttk.Label(root, text=cell.name) 
    label1.pack()
    label = ttk.Label(root, image=cell.imagen, compound=tk.BOTTOM) 
    label.pack()
    label2 = ttk.Label(root, text=cell.descripcion) 
    label2.pack()
    
    root.mainloop()
        