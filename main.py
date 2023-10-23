import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from datetime import time as dt_time
import time
import threading


def alarm():
    messagebox.showinfo("Будильник", "Пора вставать!")
    root.destroy()


def set_alarm():
    alarm_time = entry.get()
    alarm_time_obj = dt_time(int(alarm_time.split(':')[0]), int(alarm_time.split(':')[1]))
    current_time = datetime.now().time()

    if alarm_time_obj <= current_time:
        messagebox.showerror("Ошибка", "Выберите будущее время!")
    else:
        alarm_datetime = datetime.combine(datetime.today(), alarm_time_obj)
        time_difference = (alarm_datetime - datetime.now()).total_seconds()
        t = threading.Timer(time_difference, alarm)
        t.start()
        print("Будильник поставлен!")


root = tk.Tk()
root.title("Будильник")

label = tk.Label(root, text="Установите время будильника (HH:MM):")
label.pack()
entry = tk.Entry(root)
entry.pack()
set_button = tk.Button(root, text="Установить", command=set_alarm)
set_button.pack()


root.mainloop()
