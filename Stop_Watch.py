import datetime
import time
from tkinter import *
import threading

# Colors
BLUE = "#11468F"
DARK_BLUE = "#041562"
RED = "#DA1212"

# Fonts
DIGITAL = ("digital-7", "20", "normal")


class Timer:
    def __init__(self):
        self.flag = True
        self.reset_flag = False
        self.window = Tk()
        self.window.title("Stop Watch")
        self.window.geometry("500x150")
        self.window.config(bg=DARK_BLUE, padx=20, pady=20)
        self.timer = datetime.datetime(year=1, month=1, day=1)

        # Buttons
        self.start_btn = Button(text="Start", command=self.start_thread, font=DIGITAL, width=10, fg=RED, bg=BLUE,
                                highlightthickness=0)
        self.pause_btn = Button(text="Pause", command=self.pause_thread, font=DIGITAL, width=10, fg=RED, bg=BLUE,
                                highlightthickness=0)
        self.reset_btn = Button(text="Reset", command=self.reset_thread, font=DIGITAL, width=10, fg=RED, bg=BLUE,
                                highlightthickness=0)

        # Label
        self.time_label = Label(text="00:00:00", width=25, font=("digital-7", "28", "bold"),
                                bg=DARK_BLUE, fg=RED, highlightthickness=0)

        # Giving positions
        self.time_label.grid(column=0, row=0, columnspan=3, pady=10)
        self.reset_btn.grid(column=0, row=1, pady=10, padx=5)
        self.pause_btn.grid(column=1, row=1, pady=10, padx=5)
        self.start_btn.grid(column=2, row=1, pady=10, padx=5)

        self.window.mainloop()

    def start_thread(self):
        t = threading.Thread(target=self.start)
        t.setDaemon(True)
        t.start()
        self.start_btn["state"] = "disable"
        self.pause_btn["state"] = "normal"
        self.reset_btn["state"] = "normal"

    def pause_thread(self):
        t = threading.Thread(target=self.pause)
        t.setDaemon(True)
        t.start()
        self.start_btn["state"] = "normal"
        self.pause_btn["state"] = "disable"
        self.reset_btn["state"] = "normal"

    def reset_thread(self):
        t = threading.Thread(target=self.reset)
        t.setDaemon(True)
        t.start()
        self.start_btn["state"] = "normal"
        self.pause_btn["state"] = "disable"
        self.reset_btn["state"] = "disable"

    def start(self):
        self.flag = True
        while self.flag:
            self.time_label.config(text=self.timer.strftime("%H:%M:%S"))
            self.timer += datetime.timedelta(seconds=1)
            time.sleep(1)
            if self.reset_flag:
                self.reset_flag = False
                self.time_label.config(text="00:00:00")
                break

    def pause(self):
        if self.flag:
            self.flag = False

    def reset(self):
        if self.flag:
            self.reset_flag = True
            self.timer = datetime.datetime(year=1, month=1, day=1)
            self.time_label.config(text=self.timer.strftime("%H:%M:%S"))
        else:
            self.timer = datetime.datetime(year=1, month=1, day=1)
            self.time_label.config(text=self.timer.strftime("%H:%M:%S"))
            self.reset_flag = False
            self.flag = True


Timer()
