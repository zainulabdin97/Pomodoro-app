from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def button_reset():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text=" ")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def button_start():
    global reps
    reps += 1
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(WORK_MIN * 60)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_minute = math.floor(count / 60)

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        button_start()
        work_sessions = math.floor(reps / 2)
        marks = ""
        for _ in range(work_sessions):
            marks += "✔"
            check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", command=button_start, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=button_reset, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()