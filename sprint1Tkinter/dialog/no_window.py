# no_window.py
import tkinter as tk

class NoWindow:
    def __init__(self, root, question):
        self.root = root
        self.root.title("No")

        self.label = tk.Label(self.root, text=question)
        self.label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = NoWindow(root, "¿Quieres cancelar?")
    root.mainloop()
