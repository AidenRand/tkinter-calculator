from tkinter import *
from tkinter import font

root = Tk()
root.geometry("350x530")
root.config(bg="#c3c3c3")


def make_buttons():
    buttonFont = font.Font(size=14)

    modulo_btn = Button(root, width=4, height=1, text="%", font=buttonFont)
    modulo_btn.place(x=30, y=150)

    sqr_btn = Button(root, width=4, height=1, text="√", font=buttonFont)
    sqr_btn.place(x=110, y=150)

    sqr_btn = Button(root, width=4, height=1, text="x²", font=buttonFont)
    sqr_btn.place(x=190, y=150)

    ac_btn = Button(
        root,
        width=2,
        height=1,
        text="AC",
        font=buttonFont,
        fg="#aa0a0a",
        activeforeground="#aa0a0a",
    )
    ac_btn.place(x=270, y=150)

    # second row
    seven_btn = Button(root, width=4, height=2, text="7", font=buttonFont)
    seven_btn.place(x=30, y=200)

    eight_btn = Button(root, width=4, height=2, text="8", font=buttonFont)
    eight_btn.place(x=110, y=200)

    nine_btn = Button(root, width=4, height=2, text="9", font=buttonFont)
    nine_btn.place(x=190, y=200)

    div_btn = Button(root, width=2, height=2, text="÷", font=buttonFont)
    div_btn.place(x=270, y=200)

    # third row
    four_btn = Button(root, width=4, height=2, text="4", font=buttonFont)
    four_btn.place(x=30, y=280)

    five_btn = Button(root, width=4, height=2, text="5", font=buttonFont)
    five_btn.place(x=110, y=280)

    six_btn = Button(root, width=4, height=2, text="6", font=buttonFont)
    six_btn.place(x=190, y=280)

    mult_btn = Button(root, width=2, height=2, text="×", font=buttonFont)
    mult_btn.place(x=270, y=280)

    # fourth row
    one_btn = Button(root, width=4, height=2, text="1", font=buttonFont)
    one_btn.place(x=30, y=360)

    two_btn = Button(root, width=4, height=2, text="2", font=buttonFont)
    two_btn.place(x=110, y=360)

    three_btn = Button(root, width=4, height=2, text="3", font=buttonFont)
    three_btn.place(x=190, y=360)

    minus_btn = Button(root, width=2, height=2, text="–", font=buttonFont)
    minus_btn.place(x=270, y=360)

    # fifth row
    zero_btn = Button(root, width=4, height=2, text="0", font=buttonFont)
    zero_btn.place(x=30, y=440)

    decimal_btn = Button(root, width=4, height=2, text="•", font=buttonFont)
    decimal_btn.place(x=110, y=440)

    equal_btn = Button(root, width=4, height=2, text="=", font=buttonFont)
    equal_btn.place(x=190, y=440)

    plus_btn = Button(root, width=2, height=2, text="+", font=buttonFont)
    plus_btn.place(x=270, y=440)


make_buttons()


def make_output_box():
    output_box = Label(width=41, height=6, bg="#354331")
    output_box.place(x=30, y=20)


make_output_box()

root.mainloop()
