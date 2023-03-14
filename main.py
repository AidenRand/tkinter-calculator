from tkinter import *
from tkinter import font

expression = ""


def make_equation(num):
    global expression

    expression += str(num)
    equation.set(expression)


# when AC button pressed clear equation
def clear_equation():
    global expression

    expression_box.delete(0, END)
    expression = ""


def solve_equation():
    global expression

    expression_box.delete(0, END)
    equation.set(eval(expression))
    expression = ""


if __name__ == "__main__":
    root = Tk()
    root.geometry("310x380")
    root.config(bg="#c6c6c6")
    root.title("Calculator")
    root.option_add("*Button.Font", "aerial 14")
    root.option_add("*Button.width", "3")
    root.option_add("*Button.height", "1")

    equation = StringVar()

    box_font = font.Font(size=20)
    expression_box = Entry(
        root,
        textvariable=equation,
        width=16,
        bg="#354331",
        font=box_font,
    )
    expression_box.place(x=30, y=30)

    modulo_btn = Button(
        root,
        text="%",
        command=lambda: make_equation("%"),
    )
    modulo_btn.place(x=95, y=110)

    sqr_btn = Button(
        root,
        text="x^",
        command=lambda: make_equation("**"),
    )
    sqr_btn.place(x=160, y=110)

    ac_btn = Button(
        root,
        width=2,
        text="AC",
        fg="#aa0a0a",
        activeforeground="#aa0a0a",
        command=lambda: clear_equation(),
    )
    ac_btn.place(x=225, y=110)

    # second row
    seven_btn = Button(
        root,
        text="7",
        command=lambda: make_equation(7),
    )
    seven_btn.place(x=30, y=160)

    eight_btn = Button(
        root,
        text="8",
        command=lambda: make_equation(8),
    )
    eight_btn.place(x=95, y=160)

    nine_btn = Button(
        root,
        text="9",
        command=lambda: make_equation(9),
    )
    nine_btn.place(x=160, y=160)

    div_btn = Button(
        root,
        width=2,
        text="÷",
        command=lambda: make_equation("/"),
    )
    div_btn.place(x=225, y=160)

    # third row
    four_btn = Button(
        root,
        text="4",
        command=lambda: make_equation(4),
    )
    four_btn.place(x=30, y=210)

    five_btn = Button(
        root,
        text="5",
        command=lambda: make_equation(5),
    )
    five_btn.place(x=95, y=210)

    six_btn = Button(
        root,
        text="6",
        command=lambda: make_equation(6),
    )
    six_btn.place(x=160, y=210)

    mult_btn = Button(
        root,
        width=2,
        text="×",
        command=lambda: make_equation("*"),
    )
    mult_btn.place(x=225, y=210)

    # fourth row
    one_btn = Button(
        root,
        text="1",
        command=lambda: make_equation(1),
    )
    one_btn.place(x=30, y=260)

    two_btn = Button(
        root,
        text="2",
        command=lambda: make_equation(2),
    )
    two_btn.place(x=95, y=260)

    three_btn = Button(
        root,
        text="3",
        command=lambda: make_equation(3),
    )
    three_btn.place(x=160, y=260)

    minus_btn = Button(
        root,
        width=2,
        text="–",
        command=lambda: make_equation("-"),
    )
    minus_btn.place(x=225, y=260)

    # fifth row
    zero_btn = Button(
        root,
        text="0",
        command=lambda: make_equation(0),
    )
    zero_btn.place(x=30, y=310)

    decimal_btn = Button(
        root,
        text="•",
        command=lambda: make_equation("."),
    )
    decimal_btn.place(x=95, y=310)

    equal_btn = Button(root, height=1, text="=", command=solve_equation)
    equal_btn.place(x=160, y=310)

    plus_btn = Button(
        root,
        width=2,
        text="+",
        command=lambda: make_equation("+"),
    )
    plus_btn.place(x=225, y=310)

root.mainloop()
