import tkinter as tk


class App (tk.Tk):
    def __init__(self):
        super().__init__()

    def file(self):
        self.geometry('500x100')
        self.title('main')


if __name__ == "__main__":
    add = App()
    add.mainloop()
