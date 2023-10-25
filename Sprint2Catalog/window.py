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
    
    def on_button_clicked2(self):
      messagebox.showinfo("Acerca del desarrolador", "Hola")
    

    def load_image_from_url(self, url):
      response = requests.get(url)
      img_data = Image.open(BytesIO(response.content))
      img = ImageTk.PhotoImage((img_data).resize((250, 250), Image.Resampling.LANCZOS))
      return img

    def on_button_clicked(self, cell):
        detail_window = DetailWindow(cell)

    
    def __init__(self, root, json_data):
      root.title("MainWindow")
      self.root = root

      self.canvas = Canvas(root)
      self.scrollbar = Scrollbar(root, orient="vertical", command=self.canvas.yview) 
      self.scrollable_frame = Frame(self.canvas)  

      self.scrollable_frame.bind("<Configure>",lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
    
      self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw") ## Creamos la ventana en la posición 0, 0. La ancla es para que haya un ajuste del marco.
      self.canvas.configure(yscrollcommand=self.scrollbar.set) ## Configura el lienzo para emplearlo.

      self.cell_list = [] 
      for i, data in enumerate(json_data):
          name = data["name"] 
          descripcion = data["description"]
          url = data["image_url"]
          imagen = self.load_image_from_url(url)

          cell = CatalogCell(name, descripcion, url, imagen) 
          self.cell_list.append(cell)

          self.canvas.grid(row=0, column=0, sticky="nsew") ## Para colocar el lienzo:
          self.scrollbar.grid(row=0, column=1, sticky="ns") ## Para colocar la barra:
          
          root.grid_rowconfigure(0, weight=1)
          root.grid_columnconfigure(0, weight=1)
          
          frame = Frame(self.scrollable_frame) ## Marco que contendrá lo que se vaya a mostrar
          frame.pack(pady=10)
          
          label = Label(frame, image=cell.imagen, text=name, compound=tk.BOTTOM) ## Etiqueta para mostrar la imagen
          label.grid(row=0, column=0)
          
          label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))    
    
    

      for i in range(len(self.cell_list)):
          self.cell_frame.grid_rowconfigure(i, weight=1)
          x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 
          y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
          root.geometry(f"+{int(x)}+{int(y)}")

      
      barra_menus = tk.Menu()
      menu_archivo = tk.Menu(barra_menus, tearoff=False) 
        
      menu_archivo.add_command(label="Acerca de", command=self.on_button_clicked2) 
      barra_menus.add_cascade(menu=menu_archivo, label="Ayuda")
      root.config(menu=barra_menus)


  