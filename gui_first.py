from tkinter import *
import tkinter.ttk as ttk
from tkinter.colorchooser import *

root = Tk()
root.title("Hansongyi")
#root.geometry("400x300")
root.option_add("*Font", "맑은고딕")
root.resizable(False, False)

file_frame = Frame(root)
file_frame.pack()

#label1
lab1 = Label(root)
lab1.config(text = "운영체제 3조 이세희 이도형 조경우 한송이")
lab1.pack(side = "top", anchor = "sw")

#label2
lab2 = Label(root)
lab2.config(text = "Scheduling setting", font = "맑은고딕 20 bold")
lab2.pack()

#옵션 프레임
frame_option = LabelFrame(root)
frame_option.pack()

#1. SCHEDULING TYPE 옵션
lb1_width = Label(frame_option, text = "SCHEDULING TYPE", width = 15)
lb1_width.pack(side = "left")

opt_width = ["FCFS", "RR", "SPN", "SRTN", "HRRN"]
cmb_width = ttk.Combobox(frame_option, state = "readonly", values = opt_width, width = 8)
cmb_width.current(0)
cmb_width.pack(side = "left")

#2. P CORE  옵션
lb1_width = Label(frame_option, text = "P", width = 15)
lb1_width.pack(side = "left")

opt_width = ["1", "2", "3", "4"]
cmb_width = ttk.Combobox(frame_option, state = "readonly", values = opt_width, width = 8)
cmb_width.current(0)
cmb_width.pack(side = "left")

#3. E CORE  옵션
lb1_width = Label(frame_option, text = "E", width = 15)
lb1_width.pack(side = "left")

opt_width = ["1", "2", "3", "4"]
cmb_width = ttk.Combobox(frame_option, state = "readonly", values = opt_width, width = 8)
cmb_width.current(0)
cmb_width.pack(side = "left")

#4. TIMEQUANTUM
lb1_width = Label(frame_option, text = "TIMEQUANTUM", width = 15)
lb1_width.pack(side = "left")

txt = Text(frame_option, width=10, height = 1)
txt.pack(side = "left")

#5. ADD BUTTON
btn_add_file = Button(frame_option, padx = 5, pady = 5, width = 5, text = "ADD")
btn_add_file.pack(side = "left")

#6. DELETE BUTTON
btn_add_file = Button(frame_option, padx = 5, pady = 5, width = 5, text = "DELETE")
btn_add_file.pack(side = "left")

#7. RUN BUTTON
btn_add_file = Button(frame_option, padx = 5, pady = 5, width = 5, text = "RUN", bg = "yellow")
btn_add_file.pack(side = "left")


root.mainloop()