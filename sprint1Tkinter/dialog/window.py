import tkinter as tk
from yes_window import YesWindow
from no_window import NoWindow

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana de Ejemplo")

        self.label = tk.Label(self.root, text="¿Queres abrir a ventana?")
        self.label.pack()

        
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        self.yes_button = tk.Button(button_frame, text="Sí", command=self.open_yes_window)
        self.yes_button.pack(side=tk.LEFT, padx=10)

        self.no_button = tk.Button(button_frame, text="No", command=self.open_no_window)
        self.no_button.pack(side=tk.LEFT, padx=10)

    def open_yes_window(self):
        question = "¿Quieres confirmar?"
        yes_root = tk.Toplevel(self.root)
        app = YesWindow(yes_root, question)

    def open_no_window(self):
        question = "¿Quieres cancelar?"
        no_root = tk.Toplevel(self.root)
        app = NoWindow(no_root, question)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
