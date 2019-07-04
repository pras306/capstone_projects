from tkinter import Tk, Frame, StringVar, Entry, Label, OptionMenu, Button, END, Spinbox
import random
import math

root = Tk()

root.title('Happy Number')
root.geometry('600x400')

frame = Frame(root,bd=10)
frame.grid(column=0,row=0)

numbers_label = Label(frame,width=25,text='The first 8 Happy Numbers are: ')
number1_input = Entry(frame,width=5,justify='center')
number2_input = Entry(frame,width=5,justify='center')
number3_input = Entry(frame,width=5,justify='center')
number4_input = Entry(frame,width=5,justify='center')
number5_input = Entry(frame,width=5,justify='center')
number6_input = Entry(frame,width=5,justify='center')
number7_input = Entry(frame,width=5,justify='center')
number8_input = Entry(frame,width=5,justify='center')

numbers_label.grid(row=0,column=0)
number1_input.grid(row=0,column=1)
number2_input.grid(row=0,column=2)
number3_input.grid(row=0,column=3)
number4_input.grid(row=0,column=4)
number5_input.grid(row=0,column=5)
number6_input.grid(row=0,column=6)
number7_input.grid(row=0,column=7)
number8_input.grid(row=0,column=8)

def get_digits(num):
    i = 0
    while (math.floor(num / math.pow(10,i)) > 0):
        i += 1
    digits = []    
    while(i > 0):
        i -= 1
        digit = math.floor(num / math.pow(10,i))
        digits.append(digit)
        num = num - (digit * math.pow(10, i))        
    return digits

def find_sum_square_digits(rand_num):
    digits = get_digits(rand_num)    
    sum = 0
    for num in digits:
        sum += math.pow(num,2)    
    return sum    

def find_happy_numbers():    
    sums = []
    while len(sums) <= 8:
        sum = 0
        trial_count = 0
        rand_num = math.floor(random.random() * 100)
        init_num = rand_num
        while sum != 1 and trial_count < 10:
            sum = find_sum_square_digits(rand_num)       
            rand_num = sum        
            trial_count += 1
        if sum == 1 and init_num not in sums:
            sums.append(init_num)
    number1_input.delete(0,END)
    number1_input.insert(0,sums[0])
    number2_input.delete(0,END)
    number2_input.insert(0,sums[1])
    number3_input.delete(0,END)
    number3_input.insert(0,sums[2])
    number4_input.delete(0,END)
    number4_input.insert(0,sums[3])
    number5_input.delete(0,END)
    number5_input.insert(0,sums[4])
    number6_input.delete(0,END)
    number6_input.insert(0,sums[5])
    number7_input.delete(0,END)
    number7_input.insert(0,sums[6])
    number8_input.delete(0,END)
    number8_input.insert(0,sums[7])
    pass

submit_button = Button(frame,text='Submit',width=10,command=find_happy_numbers)
submit_button.grid(row=3,column=0)

root.mainloop()