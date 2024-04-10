from tkinter import *  
import datetime
import time
import winsound
from playsound import playsound
from threading import *

def Threading():
    t1=Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        set_time = f"{hours.get()}:{minute.get()}:{seconds.get()}"
        #print(set_time)
        time.sleep(1) 
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_time)
        if set_time == current_time:
            print("get up")
            playsound("winterBear.mp3")
            break
        



root = Tk()
root.geometry("500x400")
root.title("Alarm clock in python")
root.config(bg='light blue')

# A label ask user to set the time
l1 = Label(root, text="Alarm clock",font="comicsansms 30 bold",fg='green')
l1.pack(pady=20)
l2 = Label(root, text="Set your time", fg="red",font="comicsansms 15 bold" )
l2.pack()

# make a frame
f1 = Frame(root)
f1.pack()

# set the hour time
hours = StringVar(root)
hour =("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21","22", "23","24")
opt_hour = OptionMenu(f1, hours, *hour).pack(side=LEFT)
hours.set(hour[0])

# set the minute time
minute = StringVar(root)
min = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
opt_min = OptionMenu(f1, minute, *min).pack(side=LEFT)
minute.set(min[0])

# set time for second
seconds = StringVar(root)
second = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
opt_sec = OptionMenu(f1, seconds, *second).pack(side=LEFT)
seconds.set(second[0])
Button(root, text="Set Alarm", font="comicsansms 20 bold", command=Threading).pack(pady=20)




root.mainloop()