# yes_window.py
import tkinter as tk

class YesWindow:
    def __init__(self, root, question):
        self.root = root
        self.root.title("Sí")

        self.label = tk.Label(self.root, text=question)
        self.label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = YesWindow(root, "¿Quieres confirmar?")
    root.mainloop()
