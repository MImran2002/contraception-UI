# Created by Nyan in Zaw (Imran)
# Purpose: Health Communication is essential and patient-provider communication is a crucial step in  lowering
# mortality rate. One of the instrument that has been used recently is a UI tool to help decision-making.
#
# Credit: COM 286
# Reference: https://compucademy.net/python-turtle-graphics-and-tkinter-gui-programming/
import turtle
import tkinter as tk

contraception = [
    "Birth Control Implant",
    "IUD",
    "Birth Control Shot",
    "Vaginal Ring",
    "Birth Control Patch",
    "Birth Control Pill",
    "Condom",
    "Internal Condom",
    "Diaphragm",
    "Spermicide",
    "Withdrawal",
    "Abstinence",
    "Vasectomy"
]
contraception_dic = {
    "Birth Control Implant": 99,
    "IUD": 99,
    "Birth Control Shot": 96,
    "Vaginal Ring": 93,
    "Birth Control Patch": 93,
    "Birth Control Pill": 93,
    "Condom": 87,
    "Internal Condom": 79,
    "Diaphragm": 83,
    "Spermicide": 79,
    "Withdrawal": 78,
    "Abstinence": 100,
    "Vasectomy": 99
}


class App:
    def __init__(self, base):
        self.base = base
        self.base.title("Contraceptive decision-making UI")
        self.canvas = tk.Canvas(base)
        self.canvas.config(width=700, height=600)
        self.canvas.pack(side=tk.RIGHT)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("white")
        self.button = tk.Button(self.base, text="Press me", command=self.press)
        self.button.pack()
        self.clicked = tk.StringVar()
        self.clicked.set("Contraceptions")
        self.dropdown = tk.OptionMenu(self.base, self.clicked, *contraception)
        self.dropdown.pack()

        self.contraceptive_turtle = turtle.RawTurtle(self.screen, shape="circle")
        self.contraceptive_turtle.color("green")

    def percentage_ui(self, percentage_number):
        color = "blue"
        self.contraceptive_turtle.speed(0)
        percentage = 0
        for a in range(0, 451, 50):
            self.contraceptive_turtle.penup()
            self.contraceptive_turtle.goto(-250, -250 + a)
            self.contraceptive_turtle.pendown()
            for b in range(10):
                self.contraceptive_turtle.color(color)
                percentage = percentage + 1
                print(percentage)
                self.contraceptive_turtle.pendown()
                self.contraceptive_turtle.stamp()
                self.contraceptive_turtle.penup()
                self.contraceptive_turtle.forward(50)

                if percentage == percentage_number:
                    color = "red"
            self.contraceptive_turtle.hideturtle()

    def press(self):
        value = self.clicked.get()
        self.percentage_ui(contraception_dic[value])


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
