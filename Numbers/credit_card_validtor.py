from tkinter import Tk, Frame, StringVar, Entry, Label, OptionMenu, Button, END, Toplevel

root = Tk()

root.title('Credit Card Validator')
root.geometry('800x200')

frame = Frame(root,bd=10)
frame.grid(column=0,row=0)

card_label = Label(frame,width=25,text='Enter a Credit Card number: ')
card_input = Entry(frame,width=80,justify='center')


answer_label = Label(frame,width=40,text='Card Validity: ')
answer_input = Entry(frame,width=30,justify='center')
answer_label.grid(row=2,column=0)
answer_input.grid(row=2,column=1)

card_label.grid(row=0,column=0)
card_input.grid(row=0,column=1,columnspan=3)

def validate_card():
    card_number = card_input.get()    
    if len(card_number) != 16:        
        error_window = Toplevel()
        error_window.title("Error")
        error_label = Label(error_window,width=40,text="Card number is less than 16 digits.",bd=5,fg='red')
        error_label.pack()
    else :
        # Drop last digit as it is check digit
        last_digit = int(card_number[-1])
        card_number = card_number[0:15]
        odd_digits = list(int(d) for d in str(int(card_number[0::2])))
        # for d in odd_digits:

    pass

submit_button = Button(frame,text='Submit',width=10,command=validate_card)
submit_button.grid(row=1,column=2)

def clear_display():
    card_input.delete(0,END)    
    answer_input.delete(0,END)

clear_button = Button(frame, width=10,text='Clear', command=clear_display)
clear_button.grid(row=1,column=3)


root.mainloop()