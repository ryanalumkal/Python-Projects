from tkinter import *
import time 
from datetime import datetime

def update_clock():
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time = current_time
    
    print("Current Time =", current_time)
  

update_clock()
 