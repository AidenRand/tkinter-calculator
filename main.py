from tkinter import *
from tkinter import font

expression = ""


def make_equation(num):
    global expression

    expression += str(num)
    equation.set(expression)


def clear_equation():
    global expression

    expression_box.delete(0, END)
    expression = ""


def solve_eqaution():
    print(expression)


if __name__ == "__main__":
    root = Tk()
    root.geometry("350x530")
    root.config(bg="#c3c3c3")
    root.title("Calculator")

    equation = StringVar()
    buttonFont = font.Font(size=14)

    box_font = font.Font(size=20)
    expression_box = Entry(
        root,
        textvariable=equation,
        width=19,
        bg="#354331",
        font=box_font,
    )
    expression_box.place(x=30, y=20, height=120)

    modulo_btn = Button(
        root,
        width=4,
        height=1,
        text="%",
        font=buttonFont,
        command=lambda: make_equation("%"),
    )
    modulo_btn.place(x=30, y=150)

    sqr_btn = Button(
        root,
        width=4,
        height=1,
        text="√",
        font=buttonFont,
        command=lambda: make_equation("√"),
    )
    sqr_btn.place(x=110, y=150)

    sqr_btn = Button(
        root,
        width=4,
        height=1,
        text="x²",
        font=buttonFont,
        command=lambda: make_equation("²"),
    )
    sqr_btn.place(x=190, y=150)

    ac_btn = Button(
        root,
        width=2,
        height=1,
        text="AC",
        font=buttonFont,
        fg="#aa0a0a",
        activeforeground="#aa0a0a",
        command=lambda: clear_equation(),
    )
    ac_btn.place(x=270, y=150)

    # second row
    seven_btn = Button(
        root,
        width=4,
        height=2,
        text="7",
        font=buttonFont,
        command=lambda: make_equation(7),
    )
    seven_btn.place(x=30, y=200)

    eight_btn = Button(
        root,
        width=4,
        height=2,
        text="8",
        font=buttonFont,
        command=lambda: make_equation(8),
    )
    eight_btn.place(x=110, y=200)

    nine_btn = Button(
        root,
        width=4,
        height=2,
        text="9",
        font=buttonFont,
        command=lambda: make_equation(9),
    )
    nine_btn.place(x=190, y=200)

    div_btn = Button(
        root,
        width=2,
        height=2,
        text="÷",
        font=buttonFont,
        command=lambda: make_equation("÷"),
    )
    div_btn.place(x=270, y=200)

    # third row
    four_btn = Button(
        root,
        width=4,
        height=2,
        text="4",
        font=buttonFont,
        command=lambda: make_equation(4),
    )
    four_btn.place(x=30, y=280)

    five_btn = Button(
        root,
        width=4,
        height=2,
        text="5",
        font=buttonFont,
        command=lambda: make_equation(5),
    )
    five_btn.place(x=110, y=280)

    six_btn = Button(
        root,
        width=4,
        height=2,
        text="6",
        font=buttonFont,
        command=lambda: make_equation(6),
    )
    six_btn.place(x=190, y=280)

    mult_btn = Button(
        root,
        width=2,
        height=2,
        text="×",
        font=buttonFont,
        command=lambda: make_equation("×"),
    )
    mult_btn.place(x=270, y=280)

    # fourth row
    one_btn = Button(
        root,
        width=4,
        height=2,
        text="1",
        font=buttonFont,
        command=lambda: make_equation(1),
    )
    one_btn.place(x=30, y=360)

    two_btn = Button(
        root,
        width=4,
        height=2,
        text="2",
        font=buttonFont,
        command=lambda: make_equation(2),
    )
    two_btn.place(x=110, y=360)

    three_btn = Button(
        root,
        width=4,
        height=2,
        text="3",
        font=buttonFont,
        command=lambda: make_equation(3),
    )
    three_btn.place(x=190, y=360)

    minus_btn = Button(
        root,
        width=2,
        height=2,
        text="–",
        font=buttonFont,
        command=lambda: make_equation("–"),
    )
    minus_btn.place(x=270, y=360)

    # fifth row
    zero_btn = Button(
        root,
        width=4,
        height=2,
        text="0",
        font=buttonFont,
        command=lambda: make_equation(0),
    )
    zero_btn.place(x=30, y=440)

    decimal_btn = Button(
        root,
        width=4,
        height=2,
        text="•",
        font=buttonFont,
        command=lambda: make_equation("."),
    )
    decimal_btn.place(x=110, y=440)

    equal_btn = Button(
        root, width=4, height=2, text="=", font=buttonFont, command=solve_eqaution
    )
    equal_btn.place(x=190, y=440)

    plus_btn = Button(
        root,
        width=2,
        height=2,
        text="+",
        font=buttonFont,
        command=lambda: make_equation("+"),
    )
    plus_btn.place(x=270, y=440)


root.mainloop()
