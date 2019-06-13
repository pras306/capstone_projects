from tkinter import Tk, Frame, StringVar, Entry, Label, OptionMenu, Button, END, Spinbox
import time
import winsound

root = Tk()

root.title('Factorial Finder')
root.geometry('600x400')

frame = Frame(root,bd=10)
frame.grid(column=0,row=0)

number_label = Label(frame,width=25,text='Enter any number: ')
number_input = Entry(frame,width=30,justify='center')


answer_label = Label(frame,width=25,text='Factorial is: ')
answer_input = Entry(frame,width=30,justify='center')
answer_label.grid(row=2,column=0)
answer_input.grid(row=2,column=1)

number_label.grid(row=0,column=0)
number_input.grid(row=0,column=1)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def find_factorial():
    input_num = int(number_input.get())
    ans_value = factorial(input_num)
    answer_input.delete(0,END)
    answer_input.insert(0,ans_value)
    pass

submit_button = Button(frame,text='Submit',width=10,command=find_factorial)
submit_button.grid(row=3,column=0)

def clear_display():
    number_input.delete(0,END)    
    answer_input.delete(0,END)

clear_button = Button(frame, width=10,text='Clear', command=clear_display)
clear_button.grid(row=3,column=1)



root.mainloop()