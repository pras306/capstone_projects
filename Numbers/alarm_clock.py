from tkinter import Tk, Frame, StringVar, Entry, Label, OptionMenu, Button, END, Spinbox
import time
import winsound

root = Tk()

root.title('Alarm Clock')
root.geometry('600x400')

frame = Frame(root,bd=10)
frame.grid(column=0,row=0)

timer_label = Label(frame,width=20,text='Set the timer for the alarm: ',bd=5)
minutes_option = Spinbox(frame,from_ = 0, to_ = 59)
minutes_label = Label(frame,width=10,text='minutes',bd=5)
seconds_option = Spinbox(frame, from_ = 0, to_ = 59)
seconds_label = Label(frame,width=10,text='seconds',bd=5)

time_entry = Entry(frame, width=30,justify='center')

timer_label.grid(row=0,column=0)
minutes_option.grid(row=0,column=1)
minutes_label.grid(row=0,column=2)
seconds_option.grid(row=0, column=3)
seconds_label.grid(row=0,column=4)

time_entry.grid(row=1, column=1,columnspan=2)

def countdown(mins,secs):
    while mins + secs > 0:
        time.sleep(1)
        if secs == 0:
            secs = 59
            mins -= 1
        else:
            secs -=1
    timer_format = "Timer has been completed."        
    time_entry.delete(0,END)
    time_entry.insert(0,timer_format)
    winsound.PlaySound('alert.wav', winsound.SND_FILENAME)


def start_timer():
    mins = int(minutes_option.get())
    secs = int(seconds_option.get())
    countdown(mins,secs)
    pass

submit_button = Button(frame,text='Submit',width=10,command=start_timer)
submit_button.grid(row=2,column=3)

def clear_display():
    time_entry.delete(0,END)
    minutes_option.delete(0,END)
    minutes_option.insert(0,0) 
    seconds_option.delete(0,END)
    seconds_option.insert(0,0)

clear_button = Button(frame, width=10,text='Clear', command=clear_display)
clear_button.grid(row=2,column=4)

root.mainloop()