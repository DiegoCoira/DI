import tkinter as tk

class NoWindow:
    def __init__(self, root, question):
        self.root = root
        self.root.title("No")  # Set the window title to "No"

        # Create a widget to display show the question
        self.label = tk.Label(self.root, text=question)
        self.label.pack()  # Pack the label for display

if __name__ == "__main__":
    root = tk.Tk()  # Create a tkinter main window
    app = NoWindow(root, "¿Quieres cancelar?")  # Create an instance of NoWindow with a specific question
    root.mainloop()  # Start the tkinter main event loop
