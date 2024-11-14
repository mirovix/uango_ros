import tkinter as tk

from uango_connector.gui.control_app import ControlApp

if __name__ == "__main__":
    display = tk.Tk()
    app = ControlApp(display)
    app()
    display.mainloop()
