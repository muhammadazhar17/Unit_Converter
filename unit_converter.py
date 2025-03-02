# from tkinter import *
#  root  =TK()
# root.geometry("400x200")
#  userin =import
#  head = Label(root ,text="Unit converter", font=('comic sans',20))
#   head.grid(row=0,column=0,columnspan=2)

# userinput = Entry(root,textvariable= userin,font=('comic sans',20))
# userinput.grid(row=1,column=0)


# root.mainloop()

# from tkinter import ttk
# from u
# from tkinter import *nitconverter import lengthunits

# root = Tk()
# root.geometry("400x350")

# # Variable for user input
# userin = IntVar()
# resultin =IntVer()
# uf =StringVar()
# us =StringVar()
# def conv():
#     a =lengthunits.LengthUnit(f'userin.get()',f'{uf.get()}',f'{us.get()}').doconvert()
#     resultin.set(a)
# # Label for the heading
# head = Label(root, text="Unit Converter", font=('Comic Sans MS', 20))
# head.grid(row=0, column=0, columnspan=2, pady=10)

# # Input field
# userinput = Entry(root, textvariable=userin, font=('Comic Sans MS', 15), width=10)
# userinput.grid(row=1, column=0, padx=10, pady=10)

# # Combobox for unit selection
# unitfirst = ttk.Combobox(root,textvariable=uf, font=('Comic Sans MS', 20),  width=10 state="readonly")
# unitfirst["values"] = ("Meters", "Kilometers", "Miles", "Feet")  # Example units

# unitfirst.grid(row=1, column=1, padx=10, pady=10)

# result = Label(root, textvariable=resultin,font=('comic sans',20))
# result.grid(row=2,column=0)


# unitsecond = ttk.Combobox(root,textvariable=us, font=('Comic Sans MS', 15), width=10 state="readonly")
# unitsecond["values"] = ("Meters", "Kilometers", "Miles", "Feet")  # Example units
# unitsecond.grid(row=2, column=1, padx=10, pady=10)

# submit =Button(root,text= "SUBMIT",font=('comic sans' , 20),commond=conv)
# submit.grid(row=3,columnspan=2,padx=10, pady=10)

# reset =Button(root,text= "RESET",font=('comic sans' , 20))
# reset.grid(row=3,columnspan=2,padx=10, pady=10)

# root.mainloop()


# 


import streamlit as st

# Custom conversion function
def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
        "Feet": 3.28084
    }
    
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return "Invalid unit"
    
    value_in_meters = value / conversion_factors[from_unit]  # Convert to meters first
    converted_value = value_in_meters * conversion_factors[to_unit]  # Convert to target unit
    return round(converted_value, 4)

# Streamlit App
st.title("🌍 Unit Converter")

# User Input
value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

# Dropdowns for unit selection
units = ["Meters", "Kilometers", "Miles", "Feet"]
from_unit = st.selectbox("Convert from:", units)
to_unit = st.selectbox("Convert to:", units)

# Convert Button
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.success(f"✅ Converted Value: {result} {to_unit}")

# Reset Button
if st.button("Reset"):
    st.experimental_rerun()
