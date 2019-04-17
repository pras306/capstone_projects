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
        #Multiply digits in odd poitions by 2 and if product is greater than 10, sum the digits
        odd_digits = list(int(d) for d in str(int(card_number[0::2])))
        even_digits = list(int(d) for d in str(int(card_number[1::2])))
        new_odd_digits = []
        for d in odd_digits:
            new_d = str(int(d) * 2)
            if len(new_d) > 1:
                sum_of_digits = sum(list(int(digit) for digit in new_d))
                new_odd_digits.append(str(sum_of_digits))
            else:
                new_odd_digits.append(new_d)    
        #Add all the numbers
        sum_of_all_digits = sum(list(int(odd_digit) for odd_digit in new_odd_digits )) + sum(list(int(even_digit) for even_digit in even_digits ))
        modulo_ten = sum_of_all_digits % 10
        check_digit = 10 - modulo_ten
        #Compare with the last digit        
        if last_digit == check_digit:
            answer_input.delete(0,END)
            answer_input.insert(0,'Entered card number is valid')
        else:
            answer_input.delete(0,END)
            answer_input.insert(0,'Entered card number is  not valid')

submit_button = Button(frame,text='Submit',width=10,command=validate_card)
submit_button.grid(row=1,column=2)

def clear_display():
    card_input.delete(0,END)    
    answer_input.delete(0,END)

clear_button = Button(frame, width=10,text='Clear', command=clear_display)
clear_button.grid(row=1,column=3)


root.mainloop()