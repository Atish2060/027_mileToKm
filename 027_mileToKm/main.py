import tkinter
from tkinter import *

window = Tk()
window.title("Atish's Mile to KM converter")
window.minsize(height=100, width=150)
window.config(padx=5, pady= 5)

miles_text = Entry(width=5)
miles_text.grid(column = 1, row = 0)

miles_label = Label(text="Miles")
miles_label.grid(column = 2, row = 0)

equal_to_label = Label(text="equal to")
equal_to_label.grid(column = 0, row = 1)

km = Label(text= 0)
km.grid(column = 1, row = 1)

km_text = Label(text= "km")
km_text.grid(column = 2, row = 1)

def calculate_km():
    miles = int(miles_text.get())
    km_val = round(miles * 1.6093, 2)
    km.config(text=f"{km_val}")


calculate = Button(text="Calculate", command= calculate_km)
calculate.grid(column = 1, row = 2)



window.mainloop()