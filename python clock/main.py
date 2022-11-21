#Imports 
from tkinter import *
from datetime import datetime



def update_clock(): #Time
    now = datetime.now() 
    current_time = now.strftime("%I:%M:%S %p") #current time + pm/am
    time = Label(win, text=current_time, font= ('ds-digital',125), bg= "black", fg= "green") #label for time
    time.pack(fill= BOTH, expand= True)
    time.after(1000, lambda:[time.forget(),update_clock()]) #resets time every second 
    
def update_date(): #date
    now = datetime.now() 
    date = now.strftime("%m/%d/%Y") #current date in mm/dd/yyyy form
    date = Label(win, text = date, font= ('ds-digital',50), bg= "black", fg= "green") #label for date 
    date.pack(side=BOTTOM, fill= BOTH, expand = True)
    date.after(1000, lambda:[date.forget(),update_date()]) #resets date every second 


win = Tk()  # window
win.title("Digital Python Clock") 
win.minsize("1000", "400")
win.maxsize("1000", "400")


update_clock() #calls time function 
update_date() #calls date function
win.mainloop()
