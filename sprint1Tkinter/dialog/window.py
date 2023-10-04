import tkinter as tk

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana de Ejemplo")

        self.label = tk.Label(self.root, text="Hola, mundo!")
        self.label.pack()

        self.button = tk.Button(self.root, text="Haz clic", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        self.label.config(text="¡Botón clickeado!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
