from tkinter import *

window = Tk()
window.title("Miles to KM")

window.minsize(150, 150)
window.config(padx=75, pady=75)

label = Label(text=0)
label.grid(row=1, column=1)


def pressy_pressy():
    # km_conversion = input.get()/2
    label.config(text=(round(float(input.get())*1.609344, 6)))


button = Button(text="Convert", command=pressy_pressy)
button.grid(row=2, column=1)

input = Entry(width=10, justify="center")
input.focus()
input.grid(row=0, column=1)

miles_label = Label(text="Input Miles")
miles_label.grid(row=0, column=2)

km_label = Label(text="Output Kilometers")
km_label.grid(row=1, column=2)

window.mainloop()
