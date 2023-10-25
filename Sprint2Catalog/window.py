# Import necessary modules and classes from tkinter, PIL, and your custom modules
from io import BytesIO
from tkinter import Canvas, Frame, Label, Scrollbar, messagebox
import tkinter as tk
from cell import CatalogCell
from tkinter import messagebox
from PIL import Image, ImageTk
from detail_window import DetailWindow
import requests

# Define a class called MainWindow
class MainWindow():
    
    def About_the_dev(self):
      # Display an information message box when a button is clicked
      messagebox.showinfo("Acerca del desarrolador", "Hola")
    

    def load_image_from_url(self, url):
      # Load an image from a URL using the requests library and return it as a tkinter PhotoImage
      response = requests.get(url)
      img_data = Image.open(BytesIO(response.content))
      img = ImageTk.PhotoImage((img_data).resize((250, 250), Image.Resampling.LANCZOS))
      return img

    def on_button_clicked(self, cell):
      # Open a detail window when a button is clicked, passing a CatalogCell object
      detail_window = DetailWindow(cell)

    
    def __init__(self, root, json_data):
      root.title("MainWindow")
      self.root = root

      # Create a canvas with a scrollbar for scrolling
      self.canvas = Canvas(root)
      self.scrollbar = Scrollbar(root, orient="vertical", command=self.canvas.yview) 
      self.scrollable_frame = Frame(self.canvas)  

      # Configuration of the canvas scroll
      self.scrollable_frame.bind("<Configure>",lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
    
      self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
      self.canvas.configure(yscrollcommand=self.scrollbar.set)

      self.cell_list = [] 
      for i, data in enumerate(json_data):
          name = data["name"] 
          descripcion = data["description"]
          url = data["image_url"]
          imagen = self.load_image_from_url(url)

          # Create a CatalogCell object and add it to the list
          cell = CatalogCell(name, descripcion, url, imagen) 
          self.cell_list.append(cell)

          # Place widgets on the canvas and configure grid settings
          self.canvas.grid(row=0, column=0, sticky="nsew")
          self.scrollbar.grid(row=0, column=1, sticky="ns")
          
          root.grid_rowconfigure(0, weight=1)
          root.grid_columnconfigure(0, weight=1)
          
          frame = Frame(self.scrollable_frame) 
          frame.pack(pady=10)
          
          # Create a label with an image and text, and bind a click event
          label = Label(frame, image=cell.imagen, text=name, compound=tk.BOTTOM) 
          label.grid(row=0, column=0)
          
          label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))    
    

      for i in range(len(self.cell_list)):
          self.cell_frame.grid_rowconfigure(i, weight=1)
          x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 
          y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
          root.geometry(f"+{int(x)}+{int(y)}")


      # Create a menu bar with an "Acerca de" option
      barra_menus = tk.Menu()
      menu_archivo = tk.Menu(barra_menus, tearoff=False) 
        
      menu_archivo.add_command(label="Acerca de", command=self.on_button_clicked2) 
      barra_menus.add_cascade(menu=menu_archivo, label="Ayuda")
      root.config(menu=barra_menus)


  