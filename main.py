from tkinter import *
from tkinter import ttk


# Colors
bg_color1 = "#2e2e2e"
display_color = "#757575"
button_bg = "#a6a6a6"
button_txt = "#a6a6a6"

window = Tk()
window.title("Calculator")
window.geometry("235x318")
window.config(bg=bg_color1)

frame_display = Frame(window, width=235, height=50, bg=display_color)
frame_display.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=268, bg=bg_color1)
frame_body.grid(row=1, column=0)

#Buttons
b1 = Button(frame_body, text="C", width=11, height=2, bg=button_bg)
b1.place(x=0, y=0)

b2 = Button(frame_body, text="%", width=5, height=2)
b2.place(x=90, y=0)

b3 = Button(frame_body, text="/", width=5, height=2)
b3.place(x=177, y=0)


window.mainloop()
