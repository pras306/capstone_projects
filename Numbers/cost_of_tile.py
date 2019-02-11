from tkinter import Tk, Frame, Entry, Label, Button, END

##############################################################
####################Cost of tiles calulator###################
##############################################################

root = Tk()

root.title('Calculate Tile Cost')
root.geometry('600x400')

frame = Frame(root)
frame.grid(row=0)

cost_label = Label(frame, width=40, text='Enter the cost of tiles (in dollars): ', bd=5)
cost_entry = Entry(frame,width=40,justify='center')
cost_label.grid(row=0,column=0)
cost_entry.grid(row=0,column=1)

width_label = Label(frame, width=40, text='Enter width of floor (in feet): ', bd=5)
width_entry = Entry(frame,width=40,justify='center')
width_label.grid(row=1,column=0)
width_entry.grid(row=1,column=1)

height_label = Label(frame, width=40, text='Enter height of floor (in feet): ', bd=5)
height_entry = Entry(frame,width=40,justify='center')
height_label.grid(row=2,column=0)
height_entry.grid(row=2,column=1)

total_cost_label = Label(frame, width=40, text='The total cost of tiles (in dollars): ', bd=5)
total_cost_entry = Entry(frame,width=40,justify='center')
total_cost_label.grid(row=3,column=0)
total_cost_entry.grid(row=3,column=1)

def submit_clicked():
    total_cost = float(width_entry.get()) * float(height_entry.get()) * float(cost_entry.get())
    total_cost_entry.delete(0,END)
    total_cost_entry.insert(0,str(total_cost))

submit_button = Button(frame,width=10,text='Submit',command=submit_clicked)
submit_button.grid(row=4,column=0)

def clear_display():
    cost_entry.delete(0,END)
    width_entry.delete(0,END)
    height_entry.delete(0,END)
    total_cost_entry.delete(0,END)

clear_button = Button(frame, width=10,text='Clear', command=clear_display)
clear_button.grid(row=4,column=1)

root.mainloop()

# cost = int(input("Enter the cost of tiles (in dollars): "))
# width = int(input("Enter width of floor (in feet): "))
# height = int(input("Enter height of floor (in feet): "))
# total_cost = width * height * cost

# print("The cost of tiles of {0} x {1} floor is ${2}".format(width, height, total_cost))
