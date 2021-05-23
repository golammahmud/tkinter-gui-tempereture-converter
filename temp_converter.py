from functools import partial
from tkinter import *
import math
from tkinter import messagebox

width=500
height=500
root=Tk(className="Tkinter Temprature converter")
root.geometry(f'{width}x{height}')
# root.resizable(False, False)
title=Label(root, text="Temperature converter in Python",font='lucida 15 bold italic')
title.pack(side=TOP,pady=30)

def store_temp(set_temperature):
    global temp_val
    temp_val=set_temperature
    # if temp_val==c_f:
    #     button.config(text='Celsius to Fahrenheit')
    # elif temp_val==k_f:
    #     button.config(text='kelvin to Fahrenheit',bg='red')
        
    
def convert():
    temp=inputNumber.get()
    if temp =="":
        input_label.config(text='Please enter some value',foreground='red')
        
    else:
        input_label.config(text='Enter Temperature',foreground='black')
        if temp_val==c_f:
            f=float(float(temp)*9/5)+32
            result_label.config(text=f"Fahrenheit {f} °F")
            
    
        elif temp_val==k_f:
            f=float(9/5*(float(temp)- 273) + 32)
            result_label.config(text=f"Fahrenheit {f} °F")
        
        elif temp_val==f_c:
            c = float((float(temp) - 32) * 5 / 9) 
            result_label.config(text=f"Celsius {c} °C ")
        elif temp_val==c_k:
            k= float(float(temp)+ 273) 
            result_label.config(text=f"kelvin{k} °k ")
        
        elif temp_val==k_c:
            c=float(float(temp)-273)
            result_label.config(text=f"Celsius {c} °C")
            
        elif temp_val==f_k:
            K = float(5/9*(float(temp) - 32) + 273)
            result_label.config(text=f"Kelvin {K} °k")
        else:
            result_label.config(text='please select conversion type')
            

      
# label and entry field 
f=Frame(root,)
f.pack(side=TOP)
inputNumber = StringVar() 
input_label = Label(f, text ="Enter temperature",font='lucida 12 bold italic',foreground='black') 
input_entry = Entry(f, textvariable = inputNumber,font='lucida 15 bold italic',justify=CENTER) 
input_label.pack(side=TOP,pady=10)
input_entry.pack(side=TOP)
result_label = Label(f,text='Result:',font='lucida 20 italic') 
result_label.pack(side=BOTTOM,pady=10)


#drop down list
f2=Frame(root)
f2.pack(pady=20)
var = StringVar()
# drowpdownlist=["Celsius", "Fahrenheit","Kelvin"]
drowpdownlist=['Celsius to Fahrenheit','Kelvin to Fahrenheit',
               "Fahrenheit to Celsius",'Celsius to Kelvin','Kelvin to Celsius','Fahrenheit to Kelvin']
dropdrown=OptionMenu(f2,var,*drowpdownlist,command=store_temp,)
var.set(drowpdownlist[0]) 
dropdrown.pack(side=RIGHT)

# button widget
button=Button(f2,text='Convert',command=convert,font='lucida 10 bold italic',bd=5,relief=SUNKEN,activebackground='green')
button.pack(padx=5)



c_f=drowpdownlist[0]
k_f=drowpdownlist[1]
f_c=drowpdownlist[2]
c_k=drowpdownlist[3]
k_c=drowpdownlist[4]
f_k=drowpdownlist[5]

temp_val=c_f

  

root.mainloop()