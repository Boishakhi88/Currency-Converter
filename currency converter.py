from tkinter import *
from tkinter import ttk

converter = Tk()

converter.geometry("600x400")

converter.title("Currency_Converter")

OPTIONS ={
    "Australian Dollar":0.016,
    "Algerian Dinar":1.52,
    "Argentine Peso":0.96,
    "Bahraini Dinar":0.0044,
    "Bajan Dollar":0.024,
    "Bellarusian Ruble":0.031,
    "Bhutan currency":0.87,
    "Brazilian Real":0.062,
    "Brunei Dollar":0.016,
    "Canadian Dollar":0.015,
    "Chinese Yuan":0.078,
    "Colombian Peso":41.89,
    "Euro":0.0098,
    "Hong Kong Dollar":0.091,
    "Indian Rupee":0.87,
    "Japanese Yen":1.23,
    "Kuwaiti Dinar":0.0036,
    "Malaysian Ringgit":0.048,
    "Maldivian Rufiyaa":0.18,
    "Mexican Peso":0.24,
    "Poland zloty":0.044,
    "Pakistani Rupee":1.88,
    "Russian Ruble":0.89,
    "Singapore Dollar":0.016,
    "Turkish lira":0.093,
    "United States Dollar":0.012,
    "Zambian Kwacha":0.25

      }


def ok():
    price = taka.get()
    answer = variable.get()
    DICT = OPTIONS.get(answer,None)

    converted = float (DICT) * float (price)

    result.delete(1.0,END)
    result.insert(INSERT,"Price In ",INSERT,answer,INSERT," = ",INSERT,converted)


appName = Label(converter,text="Currency",font =("arial",25,"bold","underline"),fg="dark red")
appName.grid(row=1,column=0,padx=10)

appName = Label(converter,text="Converter",font =("arial",25,"bold","underline"),fg="green")
appName.grid(row=1,column=1,ipadx=10)

result=Text(converter,bg="brown",height=5,width=50,font=("arial",10,"bold"),bd=5)
result.grid(row=2,columnspan=10,padx=3)

bangladesh = Label (converter,text="Bangladeshi Taka:",font=("arial",11,"bold"),fg="blue")
bangladesh.grid(row=3,column=0)

taka= Entry(converter,bg="pink",font=("calibri",20))
taka.grid(row=3,column=1)

choice = Label (converter,text="choose country:",font=("arial",11,"bold"),fg="blue")
choice.grid(row=4,column=0)

variable = StringVar(converter)
variable.set(None)

option =OptionMenu(converter,variable,*OPTIONS)
option.grid(row=4,column=1,sticky="ew")

button= Button(converter,text="Convert",fg="red",font=("calibri",20),bg="powder blue",command = ok)
button.grid(row=4,column=2)

mainloop()
