from tkinter import *
from tkinter import ttk


# Colors
bg_color1 = "#2e2e2e"
display_color = "#757575"
button_bg = "#a6a6a6"
button_txt = "#a6a6a6"
orange = "#e87800"
white = "#ededed"

window = Tk()
window.title("Calculator")
window.geometry("235x318")
window.config(bg=bg_color1)

frame_display = Frame(window, width=235, height=50, bg=display_color)
frame_display.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=268, bg=bg_color1)
frame_body.grid(row=1, column=0)

#Buttons
c_button = Button(frame_body, text="C", width=11, height=2, bg=button_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
c_button.place(x=0, y=0)

percent_button = Button(frame_body, text="%", width=5, height=2, bg=button_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
percent_button.place(x=118, y=0)

division_button = Button(frame_body, text="/", width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
division_button.place(x=177, y=0)

b7 = Button(frame_body, text="7", width=5, height=2, bg=button_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=0, y=52)

b8 = Button(frame_body, text="8", width=5, height=2, bg=button_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=59, y=52)

b9 = Button(frame_body, text="9", width=5, height=2, bg=button_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=118, y=52)

multiply_button = Button(frame_body, text="*", width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
multiply_button.place(x=177, y=52)

b6 = Button(frame_body, text="6", width=5, height=2, bg=button_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=0, y=104)

b5 = Button(frame_body, text="5", width=5, height=2, bg=button_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=59, y=104)

b4 = Button(frame_body, text="4", width=5, height=2, bg=button_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=118, y=104)

decrease_button = Button(frame_body, text="-", width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
decrease_button.place(x=177, y=104)

b3 = Button(frame_body, text="3", width=5, height=2, bg=button_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=0, y=156)

b2 = Button(frame_body, text="2", width=5, height=2, bg=button_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=59, y=156)

b1 = Button(frame_body, text="1", width=5, height=2, bg=button_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=118, y=156)

increase_button = Button(frame_body, text="+", width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
increase_button.place(x=177, y=156)

b0 = Button(frame_body, text="0", width=11, height=2, bg=button_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b0.place(x=0, y=208)

comma_button = Button(frame_body, text=",", width=5, height=2, bg=button_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
comma_button.place(x=118, y=208)

result_button = Button(frame_body, text="=", width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
result_button.place(x=177, y=208)



window.mainloop()
