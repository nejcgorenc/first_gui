import Tkinter
import random
import tkMessageBox

window = Tkinter.Tk()

greeting = Tkinter.Label(window, text='Guess the secret number')
greeting.pack()

secret = random.randint(1, 100)

guess = Tkinter.Entry(window)
guess.pack()

def check_guess():
    if int(guess.get()) == secret:
        result_text = 'CORRECT'
    elif int(guess.get()) > secret:
        result_text = 'TOO HIGH'
    else:
        result_text = 'TOO LOW'

    tkMessageBox.showinfo('Result', result_text)

submit = Tkinter.Button(window, text='submit', command=check_guess)
submit.pack()




window.mainloop()