import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timmer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timmer():
    windows.after_cancel(timmer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timmer")
    tick_mark.config(text="")
    global reps
    reps =0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timmer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps %8==0:
        count_down(long_break_sec)
        timer_label.config(text="Long break", fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global  timmer

    min = math.floor(count/60)
    sec = count%60
    if sec <10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count >0:
        timmer = windows.after(1000, count_down, count-1)
    else:
        start_timmer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks +="✔"
        tick_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Pomodoro")
windows.config(padx=100, pady=50, bg=GREEN)


canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image= tomato_img)
timer_text =canvas.create_text(100, 130, text="00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


timer_label= Label( text="Timer",font=(FONT_NAME, 35, "bold"), bg=GREEN, fg=RED)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 15, "bold"), fg=RED, highlightthickness=0, command= start_timmer)
start_button.grid(row=2, column=0)

tick_mark = Label(font=(FONT_NAME, 18, "bold"), bg=GREEN, fg=RED)
tick_mark.grid(row=3, column=1)

reset_button = Button(text="Reset", font=(FONT_NAME, 15, "bold"), fg=RED, highlightthickness=0, command=reset_timmer)
reset_button.grid(row=2, column=2)


windows.mainloop()