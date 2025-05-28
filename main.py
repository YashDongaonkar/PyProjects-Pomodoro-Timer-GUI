from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30

reps = 0

timer = None

def formatter(num):
    if num<10:
        return f"0{num}"
    else:
        return str(num)

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps 

    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = "00:00")
    timer_label.config(text = "Timer")
    reps = 0
    check_mark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps += 1

    if reps%8 == 0:
        timer_label.config(text = "BREAK",fg = RED)
        count_down(LONG_BREAK_MIN*60)
    
    elif reps%2 == 0:
        timer_label.config(text = "BREAK", fg = PINK)
        count_down(SHORT_BREAK_MIN*60)

    else:
        timer_label.config(text = "WORK", fg = GREEN)
        count_down(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    global timer

    if count < 0:
        return
    
    mins = count//60
    secs = count%60

    mins = formatter(mins)
    secs = formatter(secs)

    canvas.itemconfig(timer_text,text = f"{mins}:{secs}")

    if count > 0:
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps//2):
            marks+="✔"
        check_mark_label.config(text = marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100,pady=50,bg=YELLOW)


timer_label = Label(text="Timer",fg = GREEN, bg = YELLOW,font = (FONT_NAME,35,"bold"))
timer_label.grid(row = 0,column=1)

canvas = Canvas(width = 200,height = 224, bg = YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image = tomato_img)
timer_text = canvas.create_text(100,130,text = "00:00",fill = "white",font = (FONT_NAME,35,"bold"))
canvas.grid(row = 1,column = 1)

start_btn = Button(text="start",highlightthickness=0,command = start_timer)
start_btn.grid(row = 2,column = 0)

reset_btn = Button(text="reset",highlightthickness=0,command = reset_timer)
reset_btn.grid(row = 2,column = 2)

check_mark_label = Label(fg = GREEN,bg = YELLOW)
check_mark_label.grid(row = 3,column = 1)


window.mainloop()