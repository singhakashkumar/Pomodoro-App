from tkinter import *
from math import floor

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        work_session = floor(REPS/2)
        marks = ''
        for _ in range(work_session):
            marks += '✓️'
        check_mark.config(text=marks, fg=GREEN, bg=YELLOW)


def reset_timer():
    global timer
    if timer is not None:
        window.after_cancel(timer)
    global REPS
    REPS = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
    check_mark.config(text="")


def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 2 == 0 and REPS != 8:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)

    elif REPS % 2 == 1:
        count_down(work_sec)
        title_label.config(text="Grind", fg=GREEN)

    elif REPS == 8:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        reset_timer()
    # count_down(70)


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=500, height=500, bg=YELLOW, highlightthickness=0)
noggler_hat = PhotoImage(file="./nogglerHat.png")
canvas.create_image(253, 250, image=noggler_hat)
timer_text = canvas.create_text(270, 270, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
