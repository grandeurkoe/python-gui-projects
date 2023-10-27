from tkinter import *

windows = Tk()
windows.title("Mile to Km Converter")
windows.minsize(width=250, height=10)
windows.config(padx=10, pady=10)

mile = IntVar()

mile_entry = Entry(textvariable=mile)
mile_entry.grid(row=0, column=1)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)
is_equal_label.config(padx=5, pady=5)

mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)
mile_label.config(padx=5, pady=5)

kilometer_value_label = Label(text="0")
kilometer_value_label.grid(row=1, column=1)

kilometer_label = Label(text="Kms")
kilometer_label.grid(row=1, column=2)
kilometer_label.config(padx=5, pady=5)


def mile_to_kilometers():
    mile_to_km = round(mile.get() * 1.60934, 2)
    kilometer_value_label.config(text=f"{mile_to_km}")


calculate_button = Button(text="Calculate", command=mile_to_kilometers)
calculate_button.grid(row=2, column=1)

windows.mainloop()
