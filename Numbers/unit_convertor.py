from tkinter import Tk, Frame, StringVar, Entry, Label, OptionMenu, Button, END

root = Tk()

root.title('Unit Convertor')
root.geometry('600x400')

frame = Frame(root,bd=10)
frame.grid(column=0,row=0)

from_unit_var = StringVar(root)
to_unit_var = StringVar(root)

choices = ['Celcius', 'Farenheit']
from_unit_var.set('Celcius')
to_unit_var.set('Farenheit')


from_unit_label = Label(frame,width=40,text='Enter the Unit you want to convert from: ',bd=5)
from_unit_menu = OptionMenu(frame,from_unit_var,*choices)
from_unit_label.grid(row=0,column=0)
from_unit_menu.grid(row=0,column=1)

to_unit_label = Label(frame,width=40,text='Enter the Unit you want to convert to: ',bd=5)
to_unit_menu = OptionMenu(frame,to_unit_var,*choices)
to_unit_label.grid(row=1,column=0)
to_unit_menu.grid(row=1,column=1)

value_label = Label(frame,width=40,text='Enter the value you want to convert: ',bd=5)
value_input = Entry(frame,width=40,justify='center',text='0')
value_label.grid(row=2,column=0)
value_input.grid(row=2,column=1)

answer_label = Label(frame,width=40,text='The converted value is: ',bd=5)
answer_input = Entry(frame,width=40,justify='center')
answer_label.grid(row=3,column=0)
answer_input.grid(row=3,column=1)

def temperature_convert():
    from_unit = from_unit_var.get()
    to_unit = 0    
    value = float(value_input.get())
    # to_unit = to_unit_var.get()
    if from_unit == 'Celcius':
        to_unit = (value * 9/5) + 32
    elif from_unit == 'Farenheit':
        to_unit = (value - 32) * 5/9
    answer_input.delete(0,END)
    answer_input.insert(0,str(to_unit))    

convert_button = Button(frame,text='Convert',width=10,command=temperature_convert)
convert_button.grid(row=4,column=1)

root.mainloop()