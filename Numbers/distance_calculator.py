from geopy.geocoders import Nominatim
from tkinter import Tk, Frame, StringVar, Entry, Label, OptionMenu, Button, END, Spinbox
from geopy.distance import geodesic

root = Tk()

root.title('Distance between two cities')
root.geometry('800x200')

frame = Frame(root,bd=10)
frame.grid(column=0,row=0)

city1_label = Label(frame,width=25,text='Enter the first city: ')
city1_input = Entry(frame,width=30,justify='center')
country1_label = Label(frame,width=25,text="Enter the first city's country: ")
country1_input = Entry(frame,width=30,justify='center')

city2_label = Label(frame,width=25,text='Enter the second city: ')
city2_input = Entry(frame,width=30,justify='center')
country2_label = Label(frame,width=25,text="Enter the second city's country: ")
country2_input = Entry(frame,width=30,justify='center')

city1_label.grid(row=0,column=0)
city1_input.grid(row=0,column=1)
country1_label.grid(row=0, column=2)
country1_input.grid(row=0, column=3)

city2_label.grid(row=1,column=0)
city2_input.grid(row=1,column=1)
country2_label.grid(row=1, column=2)
country2_input.grid(row=1, column=3)

answer_label = Label(frame,width=40,text='The converted value is: ')
answer_input = Entry(frame,width=30,justify='center')
answer_label.grid(row=2,column=0)
answer_input.grid(row=2,column=1)

def calculate_distance():
    address1 = city1_input.get() + ", " + country1_input.get()
    address2 = city2_input.get() + ", " + country2_input.get()
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location1 = geolocator.geocode(address1)
    location2 = geolocator.geocode(address2)
    
    city1_lat_long = (location1.latitude, location1.longitude)
    city2_lat_long = (location2.latitude, location2.longitude)

    cities_distance = geodesic(city1_lat_long, city2_lat_long)

    answer_input.delete(0,END)
    answer_input.insert(0,str(cities_distance))
    pass

submit_button = Button(frame,text='Submit',width=10,command=calculate_distance)
submit_button.grid(row=2,column=2)

def clear_display():
    city1_input.delete(0,END)
    city2_input.delete(0,END)
    country1_input.delete(0,END) 
    country2_input.delete(0,END)
    answer_input.delete(0,END)

clear_button = Button(frame, width=10,text='Clear', command=clear_display)
clear_button.grid(row=2,column=3)


# print((location.latitude, location.longitude))
root.mainloop()