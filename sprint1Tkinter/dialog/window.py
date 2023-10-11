import tkinter as tk
from yes_window import YesWindow
from no_window import NoWindow

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana de Ejemplo")  # Set the main window title

        # To display a question
        self.label = tk.Label(self.root, text="¿Quieres abrir la ventana?")
        self.label.pack()  # Pack the label for display

        # Frame to contain the buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        # "Yes" button with a callback to open the YesWindow
        self.yes_button = tk.Button(button_frame, text="Sí", command=self.open_yes_window)
        self.yes_button.pack(side=tk.LEFT, padx=10)

        # "No" button with a callback to open the NoWindow
        self.no_button = tk.Button(button_frame, text="No", command=self.open_no_window)
        self.no_button.pack(side=tk.LEFT, padx=10)

    # Callback function to open the YesWindow
    def open_yes_window(self):
        question = "¿Quieres confirmar?"  # Define the question for the YesWindow
        yes_root = tk.Toplevel(self.root)  # Create a new window
        app = YesWindow(yes_root, question)  # Initialize YesWindow 

    # Callback function to open the NoWindow
    def open_no_window(self):
        question = "¿Quieres cancelar?"  # Define the question for the NoWindow
        no_root = tk.Toplevel(self.root)  # Create a new window
        app = NoWindow(no_root, question)  # Initialize NoWindow

if __name__ == "__main__":
    root = tk.Tk()  # Create the main tkinter window
    app = MainWindow(root)  # Create a MainWindow class
    root.mainloop()  # Start the tkinter main event loop