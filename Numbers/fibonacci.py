from tkinter import Tk, Frame, Entry, Label, Button, END, OptionMenu, StringVar

##############################################################
#######################Generate Fibonacci#####################
##############################################################

root = Tk()

root.title('Fibonacci Generator')
root.geometry('600x400')

frame = Frame(root)
frame.grid(row=0)

choice_option = StringVar(root)
choices = ['Upto N', 'Nth number']
choice_option.set('Upto N')


convertor_type_label = Label(frame,width=40,text='Do you wish to generate Fibonacci sequence upto the number or to the Nth number?',bd=5)
chosen_option = OptionMenu(frame,choice_option,*choices)
convertor_type_label.grid(row=0,column=0)
chosen_option.grid(row=0,column=1)

digit_label = Label(frame, width=40, text='Enter the limit for the sequence: ', bd=5)
digit_entry = Entry(frame,width=40,justify='center')
digit_label.grid(row=1,column=0)
digit_entry.grid(row=1,column=1)

answer_label = Label(frame, width=40, text='The Fibonacci series is: ', bd=5)
answer_entry = Entry(frame,width=40,justify='center')
answer_label.grid(row=2,column=0)
answer_entry.grid(row=2,column=1)

def submit_clicked():
    prev_num = 1
    current_num = 1
    result_str = "1 "
    limit = int(digit_entry.get())
    choice = choice_option.get()
    if choice == "Upto N":
        while current_num <= limit:
            result_str += str(current_num) +  " "
            prev_num, current_num = current_num, current_num + prev_num
    else :
        count = 2
        while count <= limit:
            result_str += str(current_num) +  " "
            prev_num, current_num = current_num, current_num + prev_num
            count += 1
    answer_entry.delete(0,END)
    answer_entry.insert(0,result_str)
    

submit_button = Button(frame,width=10,text='Submit',command=submit_clicked)
submit_button.grid(row=3,column=0)

def clear_display():
    digit_entry.delete(0,END)
    answer_entry.delete(0,END)

clear_button = Button(frame, width=10,text='Clear', command=clear_display)
clear_button.grid(row=3,column=1)

root.mainloop()