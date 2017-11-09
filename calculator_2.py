import Tkinter
import tkMessageBox

window = Tkinter.Tk()

greeting = Tkinter.Label(window, text='Vnesi izraz:')
greeting.pack()

izraz = Tkinter.Entry(window)
izraz.pack()


def racunanje():
    string_izraz = izraz.get()
    x = ''
    run_x = True
    run_y = False
    y = ''
    for char in string_izraz:
        if run_y:
            y = y + char
        if char == '+' or char == '-' or char == '*' or char == '/':
            run_x = False
            run_y = True
            operator = char
        if run_x:
            x = x + char

    x_int = int(x)
    y_int = int(y)
    if operator == '+':
        result_text = x_int + y_int
    elif operator == '-':
        result_text = x_int - y_int
    elif operator == '*':
        result_text = x_int * y_int
    elif operator == '/':
        result_text = x_int / y_int
    else:
        result_text = 'NAPAKA'

    tkMessageBox.showinfo('Result', result_text)

submit = Tkinter.Button(window, text='IZRACUNAJ', command=racunanje)
submit.pack()

window.mainloop()