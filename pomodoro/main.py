from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
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


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    pomo_on = True

    if REPS % 8 == 0:
        countdown(long_sec)
        label_title.config(text="LONG BREAK", fg=GREEN, bg=YELLOW)

    elif REPS % 2 == 0:
        countdown(short_sec)
        label_title.config(text="SHORT BREAK", fg=PINK, bg=YELLOW)

    else:
        countdown(work_sec)
        label_title.config(text="FOCUS", fg=RED, bg=YELLOW)


def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_display, text="00:00")
    label_title.config(text="TIMER")
    label_check.config(text="")
    global REPS
    REPS = 0


def countdown(count):
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_display, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        num_ticks = REPS // 2
        tick = ""
        for i in range(num_ticks):
            tick += '✅'
        label_check.config(text=tick)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, highlightthickness=0, bg=YELLOW)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_display = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

label_title = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
label_title.grid(column=1, row=0)

label_check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
label_check.grid(column=1, row=4)

reset_button = Button(text="RESET", command=reset)
reset_button.grid(column=4, row=3)

start_button = Button(text="START", command=start_timer)
start_button.grid(column=0, row=3)

window.mainloop()
