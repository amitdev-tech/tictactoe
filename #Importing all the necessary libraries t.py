# # #Importing all the necessary libraries to form the alarm clock:
# # from tkinter import *
# # import datetime
# # import time
# # import winsound
# # def alarm(set_alarm_timer):
# #  while True:
# #         time.sleep(1)
# #         current_time = datetime.datetime.now()
# #         now = current_time.strftime("%H:%M:%S")
# #         date = current_time.strftime("%d/%m/%Y")
# #         print("The Set Date is:",date)
# #         print(now)
# #         if now == set_alarm_timer:
# #             print("Time to Wake up")
# #         winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
# #         break

# # def actual_time():
# #     set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
# #     alarm(set_alarm_timer)
# #     clock = Tk()
# #     clock.title("DataFlair Alarm Clock")
# #     clock.geometry("400x200")
# #     time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
# #     addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
# #     setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

# # # The Variables we require to set the alarm(initialization):
# #     hour = StringVar()
# #     min = StringVar()
# #     sec = StringVar()

# # #Time required to set the alarm clock:
# #     hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
# #     minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
# #     secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)

# # #To take the time input by user:
# #     submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)

# #     clock.mainloop()
# # #Execution of the window.

# #                                        *Welcome to DataFlair Alarm Clock*


# #Importing all the necessary libraries to form the alarm clock:
# from tkinter import *
# import datetime
# import time
# import winsound



# def alarm(set_alarm_timer):
#     while True:
#         time.sleep(1)
#         current_time = datetime.datetime.now()
#         now = current_time.strftime("%H:%M:%S")
#         date = current_time.strftime("%d/%m/%Y")
#         print("The Set Date is:",date)
#         print(now)
#         if now == set_alarm_timer:
#             print("Time to Wake up")
#             winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
#             break

# def actual_time():
#     set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
#     alarm(set_alarm_timer)

# clock = Tk()
# clock.title("DataFlair Alarm Clock")
# clock.iconbitmap(r"dataflair-logo.ico")
# clock.geometry("400x200")
# time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
# addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
# setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

# # The Variables we require to set the alarm(initialization):
# hour = StringVar()
# min = StringVar()
# sec = StringVar()

# #Time required to set the alarm clock:
# hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
# minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
# secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)

# #To take the time input by user:
# submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)

# clock.mainloop()
# #Execution of the window.


from tkinter import *
import datetime
import time
import winsound
def Alarm(set_alarm_timer):
   while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        cur_date = actual_time.strftime("%d/%m/%Y")
        msg="Current Time: "+str(cur_time)
        print(msg)
        if cur_time == set_alarm_timer:
            winsound.PlaySound("Music.wav",winsound.SND_ASYNC)
            break
 
def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    Alarm(alarm_set_time)
    window = Tk()
    window.title("Alarm Clock")
    window.geometry("400x160")
    window.config(bg="#922B21")
    window.resizable(width=False,height=False)
 
time_format=Label(window, text= "Remember to set time in 24 hour format!", fg="white",bg="#922B21",font=("Arial",15)).place(x=20,y=120)
 
addTime = Label(window,text = "Hour     Min     Sec",font=60,fg="white",bg="black").place(x = 210)
setYourAlarm = Label(window,text = "Set Time for Alarm: ",fg="white",bg="#922B21",relief = "solid",font=("Helevetica",15,"bold")).place(x=10, y=40)
 
hour = StringVar()
min = StringVar()
sec = StringVar()
 
hourTime= Entry(window,textvariable = hour,bg = "#48C9B0",width = 4,font=(20)).place(x=210,y=40)
minTime= Entry(window,textvariable = min,bg = "#48C9B0",width = 4,font=(20)).place(x=270,y=40)
secTime = Entry(window,textvariable = sec,bg = "#48C9B0",width = 4,font=(20)).place(x=330,y=40)
 
submit = Button(window,text = "Set Your Alarm",fg="Black",bg="#D4AC0D",width = 15,command = get_alarm_time,font=(20)).place(x =100,y=80)
 
window.mainloop()
    