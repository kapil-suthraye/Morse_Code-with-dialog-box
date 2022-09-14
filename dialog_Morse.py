from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

window = Tk()
window.geometry('300x300')
l1 = Label(window, text="morse")
window.title('THE MORSE CODE TRANSLATOR')
window.configure(bg='White')
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', '#': '...---'}


def buttonfunction():  # encrytion:English->Morse code
    message = simpledialog.askstring("morse code", "Enter English Code")
    message = message.upper()
    cipher = ''
    for letter in message:
        if letter != ' ':

            cipher += MORSE_CODE_DICT[letter] + ' '
        else:

            cipher += ' '

    labe1 = Label(text=cipher, font=10000, bg='skyblue').pack()


def but():  # decryption:Morse Code->English
    message = simpledialog.askstring("morse code", "Enter Morse Code")

    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        if (letter != ' '):

            i = 0

            citext += letter


        else:

            i += 1

            if i == 2:

                decipher += ' '
            else:

                try:

                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                                  .values()).index(citext)]
                    citext = ''
                except:
                    messagebox.showinfo('question', 'the code is incorrect')
    lan = Label(text=decipher, font=20).pack()


b = Button(window, text="ENGLISH to MORSE CODE", command=buttonfunction, bg='pink')
b.pack()
b1 = Button(window, text="MORSE CODE to ENGLISH", command=but, bg='orange').pack(side=RIGHT)

window.mainloop()
