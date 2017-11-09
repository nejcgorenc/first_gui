import Tkinter
import tkMessageBox

window = Tkinter.Tk()

greeting = Tkinter.Label(window, text='Vnesi x:')
greeting.pack()

x = Tkinter.Entry(window)
x.pack()

greeting1 = Tkinter.Label(window, text='Vnesi operacijo (+ - * /):')
greeting1.pack()

operator = Tkinter.Entry(window)
operator.pack()

greeting2 = Tkinter.Label(window, text='Vnesi y:')
greeting2.pack()

y = Tkinter.Entry(window)
y.pack()

def racunanje():
    x_int = int(x.get())
    y_int = int(y.get())
    if operator.get() == '+':
        result_text = x_int + y_int
    elif operator.get() == '-':
        result_text = x_int - y_int
    elif operator.get() == '*':
        result_text = x_int * y_int
    elif operator.get() == '/':
        result_text = x_int / y_int
    else:
        result_text = 'NAPAKA'

    tkMessageBox.showinfo('Result', result_text)

submit = Tkinter.Button(window, text='submit', command=racunanje)
submit.pack()

window.mainloop()