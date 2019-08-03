from tkinter import *
import tkinter.messagebox
from finalizing import *
#from recordForRegistration import *
from prediction import *

global s
window = Tk()
window.geometry("600x600")
window.title("testing")

def printt():
    first = fn.get()
    second = ln.get()
    dob1 = dob.get()
    gen = radio_var.get()
    s = f"{first}{second}{dob1}{gen}"
    print(s)
    #tkinter.messagebox.showinfo("welcome", 'user is registered!!')
    return s




def exit1():
    exit()

def destro():
    window.destroy()


def checking_window():
    win = Tk()
    win.title("welcome to the prediction")
    win.geometry("600x600")
    label5 = Label(win, text="let's check your voice prediction")
    label5.place(x=30, y=70)
    butn1 = Button(win, text='Record voice', width=12, command=getAudio)
    butn1.place(x=60, y=120)
    butn2 = Button(win, text='mack image', width=12, command=create_img)
    butn2.place(x=180, y=120)
    butn3 = Button(win, text='delete voice', width=12, command=delt)
    butn3.place(x=300, y=120)
    butn4 = Button(win, text='Predict', width=12, command=make_pred)
    butn4.place(x=450, y=120)
    
    butn5 = Button(win, text='Exit', width=12, command=exit1)
    butn5.place(x=220, y=400)
    
    label8 =  Label(win, text='you are:')
    label8.grid(row=43, column=0)
    label8.place(x=100, y=300)
    predEntry =  Entry(win, width=40)
    predEntry.grid(row=43, column=1, columnspan=4)
    predEntry.focus()
    predEntry.delete(0, END)
    Output = make_pred()
    predEntry.insert(0, Output)
    predEntry.place(x=160, y=300)


fn = StringVar()
ln = StringVar()
dob = StringVar()
radio_var = StringVar()

label = Label(window, text = "registration form")
label.place(x=90, y =53)

label1 = Label(window, text = "fname:-")
label1.place(x=70, y =130)
entry1 = Entry(window, textvar = fn)
entry1.place(x=130, y=132)


label2 = Label(window, text = "lname:-")
label2.place(x=70, y =170)
entry1 = Entry(window, textvar = ln)
entry1.place(x=130, y=172)


label3 = Label(window, text = "dob:-")
label3.place(x=70, y =210)
entry3 = Entry(window, textvar = dob)
entry3.place(x=130, y=212)


label4 = Label(window, text = "gender :-")
label4.place(x=70, y=242)

r1 = Radiobutton(window, text="Male", variable=radio_var, value="Male")
r1.place(x=130, y=245)
r2 = Radiobutton(window, text="Female", variable=radio_var, value="Female")
r2.place(x=200, y=245)



lbl = Label(window, text = "click the recordVoice button")
lbl.place(x=70, y=280)
btn = Button(window, text='recordVoice', width=12, command=destro)
btn.place(x=70, y=310)

b3 = Button(window, text='predict voice', width=12, command=checking_window)
b3.place(x=220, y=500)


window.mainloop()
