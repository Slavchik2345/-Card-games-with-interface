import tkinter as tk
import random

class GuessGame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.number = self._generate_random_number()
        self.label = tk.Label(self, text=self.number)
        self.label.pack()

        self.up_button = tk.Button(self, text="Больше", command=self.up)
        self.up_button.pack()

        self.down_button = tk.Button(self, text="Меньше", command=self.down)
        self.down_button.pack()

        self.reset_button = tk.Button(self, text="Перезапустить", command=self.reset)
        self.reset_button.pack()

        self.status_label = None

    def _generate_random_number(self):
        return random.randint(1, 100)

    def up(self):
        new_number = self._generate_random_number()
        self.label["text"] = new_number
        if new_number > self.number:
            self.win()
        else:
            self.lose()

    def down(self):
        new_number = self._generate_random_number()
        self.label["text"] = new_number
        if new_number < self.number:
            self.win()
        else:
            self.lose()

    def win(self):
        self._disable_buttons()
        self.status_label = tk.Label(self, text="Победа!")
        self.status_label.pack()

    def lose(self):
        self._disable_buttons()
        self.status_label = tk.Label(self, text="Поражение!")
        self.status_label.pack()

    def reset(self):
        self.number = self._generate_random_number()
        self.label["text"] = self.number
        self._enable_buttons()
        if self.status_label is not None:
            self.status_label.destroy()

    def _disable_buttons(self):
        self.up_button["state"] = "disabled"
        self.down_button["state"] = "disabled"

    def _enable_buttons(self):
        self.up_button["state"] = "normal"
        self.down_button["state"] = "normal"

root = tk.Tk()
root.geometry("350x400")
game = GuessGame(root)
root.mainloop()