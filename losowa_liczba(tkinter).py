import tkinter
from tkinter import *
import random


def check():
    global success, try_count, random_number

    def reset():
        global success, try_count, random_number

        if 'less_label' in locals():
            less_label.destroy()
        if 'more_label' in locals():
            more_label.destroy()
        if success == 1:
            quit_button.destroy()
            win_label.destroy()
            random_number = random.randint(1, 100)
            success = False
            try_count = 0

        try_label.destroy()
        feedback.destroy()
        retry_button.destroy()
        check()

    if box.get().isdigit() and 0 < int(box.get()) <= 100:
        box_input = int(box.get())
        feedback = Label(window, text="Twoja liczba: " + str(box_input))
    else:
        box_input = -1
        feedback = Label(window, text="Możesz wpisywać tylko liczby w zakresie od 1 do 100")

    box.delete(0, 'end')
    feedback.pack()

    if 0 < box_input < random_number:
        less_label = Label(window, text="za mała liczba", fg="red")
        less_label.pack()
        try_count += 1

    if box_input > random_number:
        more_label = Label(window, text="za duża liczba", fg="red")
        more_label.pack()
        try_count += 1

    if box_input == random_number:
        win_label = Label(window, text="brawo, mój przyjacielu", fg="orange")
        win_label.pack()
        success = True
        try_count += 1

    try_label = Label(window, text="Ilość prób: " + str(try_count), fg="green")
    try_label.pack()
    

    check_button.destroy()

    if success:
        quit_button = tkinter.Button(window, text="Zakończ grę", bg="red", command=esc)
        quit_button.pack()

    retry_button = tkinter.Button(window, text="Spróbuj jeszcze raz!", command=reset)
    retry_button.pack()


def esc():
    window.destroy()


success = 0
try_count = 0
random_number = random.randint(1, 100)

window = Tk()
window.title("Moduł I, temat 8")

task = Label(window, text="Wpisz liczbe")
task.pack()

box = Entry(window, bd=5)
box.pack()

check_button = tkinter.Button(window, text="Sprawdź czy trafiłeś!", command=check)
check_button.pack()

window.mainloop()



