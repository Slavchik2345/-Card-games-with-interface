from tkinter import *
import random

class SlotMachine:
    def __init__(self, master):
        self.master = master
        self.master.title("Игровой автомат")

        self.display = Label(master, text="", font=("Helvetica", 48))
        self.display.pack(pady=20)

        self.spin_button = Button(master, text="Крутить", command=self.spin)
        self.spin_button.pack(pady=10)

        self.result = Label(master, text="", font=("Helvetica", 24))
        self.result.pack(pady=10)

    def spin(self):
        numbers = [random.randint(0, 9) for _ in range(3)]
        self.display.config(text=" ".join(map(str, numbers)))

        if numbers[0] == numbers[1] == numbers[2]:
            self.result.config(text="ПОБЕДА!")
        else:
            self.result.config(text="ПОРАЖЕНИЕ!")

root = Tk()
slot_machine = SlotMachine(root)

root.mainloop()

