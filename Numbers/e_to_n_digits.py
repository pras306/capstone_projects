import math
from tkinter import Tk, Frame, Entry, Label, Toplevel, Button, END

##############################################################
#######################e to N Digits##########################
##############################################################

root = Tk()

root.title('e to N Digits')
root.geometry('600x400')

frame = Frame(root)
frame.grid(row=0)

digit_label = Label(frame, width=40, text='Enter how many digits of e you wish to see? ', bd=5)
digit_entry = Entry(frame,width=40,justify='center')
digit_label.grid(row=0,column=0)
digit_entry.grid(row=0,column=1)

answer_label = Label(frame, width=40, text='The value of e upto specified didgit is: ', bd=5)
answer_entry = Entry(frame,width=40,justify='center')
answer_label.grid(row=1,column=0)
answer_entry.grid(row=1,column=1)

def roundoff(num, limit):
    strlist = str(num)[0:limit + 2]
    return strlist

def submit_clicked():
    digit = int(digit_entry.get())
    if digit > 15:
        error_window = Toplevel()
        error_window.title("Error")
        error_label = Label(error_window,width=40,text="Program has an upper limit to print till 15 digits only",bd=5,fg='red')
        error_label.pack()
    else:
        num = math.e
        result = roundoff(num,digit)
        answer_entry.delete(0,END)
        answer_entry.insert(0,str(result))

submit_button = Button(frame,width=10,text='Submit',command=submit_clicked)
submit_button.grid(row=2,column=0)

def clear_display():
    digit_entry.delete(0,END)
    answer_entry.delete(0,END)

clear_button = Button(frame, width=10,text='Clear', command=clear_display)
clear_button.grid(row=2,column=1)

root.mainloop()