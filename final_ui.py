from tkinter import *
import os
import sys



dir_list = ["data/training_data/", "data/test_data/"]
for i in dir_list:
	if not os.path.exists(i):
		os.makedirs(i)


        
def forReg():
    os.system('python recordForRegistration.py')

def forTest():
    os.system('python recordForTest.py')

def destro():
    window.destroy()


window = Tk()
window.geometry("600x600")
window.title("well come to the speaker Identification by jeet")
button1=Button(window, text='RecordForReg',width=15, fg='blue', command=forReg).place(x=170, y=400)
button2=Button(window, text='RecordForTest',width=15, fg='blue', command=forTest).place(x=330, y=400)
button3 = Button(window, text='Exit', width=12, fg='red', command=destro).place(x=250, y=500)




window.mainloop()
