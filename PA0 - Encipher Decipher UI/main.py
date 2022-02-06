import tkinter.font
from tkinter import *

## Dictionary for mapping the 
## alphabet to reverse alphabet
dictionary= {
    "A": "Z",
    "B": "Y",
    "C": "X",
    "D": "W",
    "E": "V",
    "F": "U",
    "G": "T",
    "H": "S",
    "I": "R",
    "J": "Q",
    "K": "P",
    "L": "O",
    "M": "N",
    "N": "M",
    "O": "L",
    "P": "K",
    "Q": "J",
    "R": "I",
    "S": "H",
    "T": "G",
    "U": "F",
    "V": "E",
    "W": "D",
    "X": "C",
    "Y": "B",
    "Z": "A",
    " ": " ",
    "\n": "\n"
}

def cipher():
    '''Function for changing the text to cipher'''
    global expression
    expression = area.get('1.0', END)
    print(expression)
    cipher_equation = ""
    for i in expression:
        if i.islower():
            cipher_equation += dictionary[i.upper()].lower()
        else:
            cipher_equation += dictionary[i]
    area2.delete('1.0', END)
    area2.insert(END, cipher_equation)

# Initiating the tkinter GUI, creating the window
root=Tk()
root.title("Cipher UI")

# Creating the frame inside the window
frame = Frame(root)
frame.pack()
frame.grid()
frame.configure(bg="light green")
font= tkinter.font.Font(size=12, family='Comic Sans MS')

### Text area for the input
area = Text(frame,width= 30, height = 5,font= font ,bd=10)
area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

### Text area for cipher text
area2= Text(frame,width= 30, height = 5,font=font ,bd=10)
area2.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

###Creating the Button
button= Button(frame,command  = lambda: cipher(),  text = "Cipher Text", bg= 'wheat3', fg="black", 
                activebackground='white', font= font)
button.grid(row=1,column=0, padx=5, pady=5)

frame.mainloop()