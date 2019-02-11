from tkinter import Tk, Entry, Frame, StringVar, Label, Button, END, Toplevel

##############################################################
##########################Change Return#######################
##############################################################

root = Tk()

root.title('Change Return Calculator')
root.geometry('600x400')

frame = Frame(root)
frame.grid(row=0)

cost_label = Label(frame,width=40,text='Enter the total cost (in dollars): ',bd=5)
cost_entry = Entry(frame,width=40,justify='center')
cost_label.grid(row=0,column=0)
cost_entry.grid(row=0,column=1)

amount_given_label = Label(frame,width=40,text='Enter the amount paid by the user (in dollars): ',bd=5)
amount_given_entry = Entry(frame,width=40,justify='center')
amount_given_label.grid(row=1,column=0)
amount_given_entry.grid(row=1,column=1)

quarters_label = Label(frame,width=40,text='The number of quarters returned is: ',bd=5)
quarters_entry = Entry(frame,width=40,justify='center')
quarters_label.grid(row=2,column=0)
quarters_entry.grid(row=2,column=1)

dimes_label = Label(frame,width=40,text='The number of dimes returned is: ',bd=5)
dimes_entry = Entry(frame,width=40,justify='center')
dimes_label.grid(row=3,column=0)
dimes_entry.grid(row=3,column=1)

nickels_label = Label(frame,width=40,text='The number of nickels returned is: ',bd=5)
nickels_entry = Entry(frame,width=40,justify='center')
nickels_label.grid(row=4,column=0)
nickels_entry.grid(row=4,column=1)

pennies_label = Label(frame,width=40,text='The number of pennies returned is: ',bd=5)
pennies_entry = Entry(frame,width=40,justify='center')
pennies_label.grid(row=5,column=0)
pennies_entry.grid(row=5,column=1)

def submit_clicked():
    cost = float(cost_entry.get())
    amount_given = float(amount_given_entry.get())

    if cost > amount_given:
        error_window = Toplevel()
        error_window.title("Error")
        error_label = Label(error_window,width=40,text="User has not paid the entire amount.",bd=5,fg='red')
        error_label.pack()
    else:
        quarters = 0
        dimes = 0
        nickels = 0
        pennies = 0
        
        change_amount = round(amount_given - cost, 2)
        cents = round(change_amount % 1, 2)

        while(cents > 0):
            if cents >= 0.25:
                quarters += 1
                cents = round(cents - 0.25, 2)
            elif cents < 0.25 and cents >= 0.10:
                dimes += 1
                cents = round(cents - 0.10, 2)
            elif cents < 0.10 and cents >= 0.05:
                nickels += 1
                cents = round(cents - 0.05, 2)
            else:
                pennies += 1
                cents = round(cents - 0.01, 2)
        quarters_entry.delete(0,END)
        quarters_entry.insert(0,str(quarters))

        dimes_entry.delete(0,END)
        dimes_entry.insert(0,str(dimes))

        nickels_entry.delete(0,END)
        nickels_entry.insert(0,str(nickels))

        pennies_entry.delete(0,END)
        pennies_entry.insert(0,str(pennies))


submit_button = Button(frame,width=10,text='Submit',command=submit_clicked)
submit_button.grid(row=6,column=0)

def clear_display():
    cost_entry.delete(0,END)
    amount_given_entry.delete(0,END)
    quarters_entry.delete(0,END)
    dimes_entry.delete(0,END)
    nickels_entry.delete(0,END)
    pennies_entry.delete(0,END)

clear_button = Button(frame, width=10,text='Clear', command=clear_display)
clear_button.grid(row=6,column=1)

# while cost > amount_given:
#     print("User has not paid the entire amount.")
#     cost = float(input("Enter the total cost (in dollars): "))

# change_amount = round(amount_given - cost, 2) 

# print("The change to be returned is {0}".format(change_amount))

# cents = round(change_amount % 1, 2)

# while(cents > 0):
#     if cents >= 0.25:
#         quarters += 1
#         cents = round(cents - 0.25, 2)
#     elif cents < 0.25 and cents >= 0.10:
#         dimes += 1
#         cents = round(cents - 0.10, 2)
#     elif cents < 0.10 and cents >= 0.05:
#         nickels += 1
#         cents = round(cents - 0.05, 2)
#     else:
#         pennies += 1
#         cents = round(cents - 0.01, 2)        
    
# print("The number of quarters is {0}, dimes is {1}, nickels is {2} and pennies is {3}".format(quarters, dimes, nickels, pennies))


root.mainloop()