from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
WORK_SEC = 0
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    start_timer_button["state"] = "active"
    global REPS
    windows.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="{:02d}".format(WORK_MIN) + ":" + "{:02d}".format(WORK_SEC))
    progress_label.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_timer_button["state"] = "disabled"
    global REPS
    REPS += 1
    if REPS == 8:
        timer_label.config(text="Break", fg=RED)
        timer_countdown(LONG_BREAK_MIN - 1, 59)
    elif REPS % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        timer_countdown(SHORT_BREAK_MIN - 1, 59)
    else:
        timer_label.config(text="Work", fg=GREEN)
        timer_countdown(WORK_MIN - 1, 59)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer_countdown(minutes, seconds):
    global timer
    canvas.itemconfig(timer_text, text="{:02d}".format(minutes) + ":" + "{:02d}".format(seconds))
    if seconds > 0:
        timer = windows.after(1000, timer_countdown, minutes, seconds - 1)
    else:
        if minutes > 0:
            timer = windows.after(1000, timer_countdown, minutes - 1, 59)
        else:
            start_timer()
            if REPS % 2 == 0:
                progress_label['text'] += "✔"


# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Pomodoro Timer")
windows.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

# Creates a canvas over which we can overlap different elements.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# We use the PhotoImage class to read through the "tomato.png" image file.
pomodoro_img = PhotoImage(file="tomato.png")

# Places the pomodoro_img at the specified location.
canvas.create_image((100, 112), image=pomodoro_img)

# Places the appropriate text at the designated location.
timer_text = canvas.create_text((100, 130), text=f"{WORK_MIN}" + ":" + "{:02d}".format(WORK_SEC), fill="white",
                                font=(FONT_NAME, 30, "bold"))

# Pack the canvas so it appears on the window.
canvas.grid(row=1, column=1)

start_timer_button = Button(text="Start", height=1, width=5, font=(FONT_NAME, 8, "bold"), borderwidth=0,
                            command=start_timer)
start_timer_button.grid(row=2, column=0)

reset_timer_button = Button(text="Reset", height=1, width=5, font=(FONT_NAME, 8, "bold"), borderwidth=0,
                            command=reset_timer)
reset_timer_button.grid(row=2, column=2)

progress_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
progress_label.grid(row=3, column=1)

windows.mainloop()
