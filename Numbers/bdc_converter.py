import re
from tkinter import Tk, Frame, StringVar, Entry, Label, OptionMenu, Button, END, Toplevel

##############################################################
######Binary to Decimal and Decimal to Binary Convertor#######
##############################################################

root = Tk()

root.title('Unit Convertor')
root.geometry('500x400')

frame = Frame(root)
frame.grid(row=0)

conversion_type = StringVar(root)
choices = ['Decimal to Binary', 'Binary to Decimal']
conversion_type.set('Decimal to Binary')


convertor_type_label = Label(frame,width=40,text='Please select the type of conversion you wish to do',bd=5)
chosen_option = OptionMenu(frame,conversion_type,*choices)
convertor_type_label.grid(row=0,column=0)
chosen_option.grid(row=0,column=1)

from_value_label = Label(frame,width=40,text='Enter the value to be converted: ', bd=5)
from_value_input = Entry(frame,width=40,justify='center')
from_value_label.grid(row=1,column=0)
from_value_input.grid(row=1,column=1)

to_value_label = Label(frame,width=40,text='The converted value is: ', bd=5)
to_value_input = Entry(frame,width=40,justify='center')
to_value_label.grid(row=2,column=0)
to_value_input.grid(row=2,column=1)

def convert():
    '''
    Converts binary to decimal and decimal to binary based on the option 
    chosen in OptionMenu() in the tkinter GUI
    '''
    from_type = conversion_type.get()
    from_value = int(from_value_input.get())
    to_value = ''   
    if from_type == 'Decimal to Binary':
        while from_value != 1:
            reminder = from_value % 2
            from_value = int(from_value / 2)
            to_value += str(reminder)

        to_value += str(from_value)
        to_value = to_value[::-1]
        to_value_input.delete(0,END)
        to_value_input.insert(0,to_value)
    elif from_type == 'Binary to Decimal':
        binary_val = str(from_value)
        if re.search('[2-9A-Za-z]+', binary_val) != None:
            error_window = Toplevel()
            error_window.title("Error")
            error_label = Label(error_window,width=40,text="Please enter a value containing 0's and 1's alone.",bd=5,fg='red')
            error_label.pack()
        else:            
            binary_val = binary_val[::-1]
            index = 0
            decimal_val = 0
            for char in binary_val:
                decimal_val += (2 ** index) * int(char)
                index += 1
            to_value_input.delete(0,END)
            to_value_input.insert(0,str(decimal_val))

convert_button = Button(frame,text='Convert',width=10,command=convert)
convert_button.grid(row=3,column=1)


root.mainloop()