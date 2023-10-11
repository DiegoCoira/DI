import tkinter as tk

class YesWindow:
    def __init(self, root, question):
        self.root = root
        self.root.title("Sí")  # Set the window title to "Sí"

        # Create a widget to display the question
        self.label = tk.Label(self.root, text=question)
        self.label.pack()  # Pack the label for display

if __name__ == "__main__":
    root = tk.Tk()  # Create a tkinter main window
    app = YesWindow(root, "¿Quieres confirmar?")  # Create an instance of NoWindow with a specific question
    root.mainloop()  # Start the tkinter main event loop
