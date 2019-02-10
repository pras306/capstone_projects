from tkinter import Tk, Frame, StringVar, Entry, Label, OptionMenu, Button, END

top = Tk()

top.title('Calculator')
top.geometry('400x300')

frame = Frame(top, bd=15)
frame.grid(row=0)

# ment = StringVar()
# result = StringVar()

E1 = Entry(frame,width=40, justify='right')
E1.grid(row=0,columnspan=4)

def display_text(input_txt):
    # value = ment.get()
    if E1['text'] == '0':
        value = input_txt
    else:
        if input_txt in ['+','-','x','/']:
            value = E1['text'] + ' ' +  input_txt         
        else:
            value = E1['text'] +  input_txt 
    E1['text'] = value
    E1.delete(0,END)
    E1.insert(0,value)

def clear_display():
    E1.delete(0,END)
    E1['text'] = ''

def display_back():
    if len(E1['text']) == 1:
        clear_display()
    else:
        E1.delete(0,END)    
        E1.insert(0,E1['text'][0:len(E1['text'])-1])
        E1['text'] = E1['text'][0:len(E1['text'])-1]

def display_sqrt():
    value = float(E1['text'])
    sqrt_val = value ** 0.5
    E1.delete(0,END)    
    E1.insert(0,str(sqrt_val))
    E1['text'] = str(sqrt_val)

def perform_operation():
    disp_val = E1['text']    
    if disp_val.find('+') >= 0:
        lst = [float(x) for x in disp_val.split('+')]        
        display_sum(lst)
    elif disp_val.find('-') >= 0:
        lst = [float(x) for x in disp_val.split('-')]        
        display_minus(lst)
    elif disp_val.find('x') >= 0:
        lst = [float(x) for x in disp_val.split('x')]        
        display_product(lst)
    elif disp_val.find('/') >= 0:
        lst = [float(x) for x in disp_val.split('/')]        
        display_division(lst)

def display_sum(sum_lst):
    total = 0
    for num in sum_lst:
        total += num
    E1.delete(0,END)    
    E1.insert(0,str(total))
    E1['text'] = str(total)

def display_minus(minus_lst):
    total = minus_lst[0]    
    for num in minus_lst[1::]:
        total -= num    
    E1.delete(0,END)    
    E1.insert(0,str(total))
    E1['text'] = str(total)

def display_product(prod_lst):
    total = prod_lst[0]    
    for num in prod_lst[1::]:
        total *= num    
    E1.delete(0,END)    
    E1.insert(0,str(total))
    E1['text'] = str(total)

def display_division(div_lst):
    total = div_lst[0]    
    for num in div_lst[1::]:
        total /= num    
    E1.delete(0,END)    
    E1.insert(0,str(total))
    E1['text'] = str(total)

b1 = Button(frame,text='sqrt',width=10,command=display_sqrt)
b2 = Button(frame,text='C',width=10,command=clear_display)
b3 = Button(frame,text='back',width=10,command=display_back)
b4 = Button(frame,text='/',width=10,command=lambda: display_text(b4['text']))

b5 = Button(frame,text='7',width=10,command=lambda: display_text(b5['text']))
b6 = Button(frame,text='8',width=10,command=lambda: display_text(b6['text']))
b7 = Button(frame,text='9',width=10,command=lambda: display_text(b7['text']))
b8 = Button(frame,text='x',width=10,command=lambda: display_text(b8['text']))

b9 = Button(frame,text='4',width=10,command=lambda: display_text(b9['text']))
b10 = Button(frame,text='5',width=10,command=lambda: display_text(b10['text']))
b11 = Button(frame,text='6',width=10,command=lambda: display_text(b11['text']))
b12 = Button(frame,text='-',width=10,command=lambda: display_text(b12['text']))

b13 = Button(frame,text='1',width=10,command=lambda: display_text(b13['text']))
b14 = Button(frame,text='2',width=10,command=lambda: display_text(b14['text']))
b15 = Button(frame,text='3',width=10,command=lambda: display_text(b15['text']))
b16 = Button(frame,text='+',width=10,command=lambda: display_text(b16['text']))

b17 = Button(frame,text='0',width=20,command=lambda: display_text(b17['text']))
b18 = Button(frame,text='.',width=10,command=lambda: display_text(b18['text']))
b19 = Button(frame,text='=',width=10,command=perform_operation)

b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
b4.grid(row=1, column=3)
b5.grid(row=2, column=0)
b6.grid(row=2, column=1)
b7.grid(row=2, column=2)
b8.grid(row=2, column=3)
b9.grid(row=3, column=0)
b10.grid(row=3,column=1)
b11.grid(row=3,column=2)
b12.grid(row=3,column=3)
b13.grid(row=4, column=0)
b14.grid(row=4,column=1)
b15.grid(row=4,column=2)
b16.grid(row=4,column=3)
b17.grid(row=5,columnspan=2)
b18.grid(row=5,column=2)
b19.grid(row=5,column=3)

top.mainloop()