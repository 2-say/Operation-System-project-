from tkinter import *
import tkinter.ttk as ttk
from tkinter.colorchooser import *

root = Tk()
root.title("Hansongyi")
root.geometry("1200x500")
root.option_add("*Font", "맑은고딕 9")
root.resizable(False, False)

file_frame = Frame(root)
file_frame.pack()

# lab_team_project
lab_team_project = Label(root)
lab_team_project.config(text="운영체제 3조 이세희 이도형 조경우 한송이")
lab_team_project.pack(side="top", anchor="sw")

# lab_topic
lab_topic = Label(root)
lab_topic.config(text="Scheduling setting", font="맑은고딕 20 bold")
lab_topic.pack()

# INPUT 프레임
input_frame = LabelFrame(root)
input_frame.pack()

# PROCESS 프레임
process_frame = LabelFrame(root)
process_frame.pack()

# PROCESSOR 프레임
processor_frame = LabelFrame(root)
processor_frame.pack()

# SCHEDULING TYPE 옵션
lab_scheduling_type = Label(input_frame, text="SCHEDULING TYPE", width=15)
lab_scheduling_type.grid(column = 1, row = 0, padx = 10, pady = 10)

opt_scheduling_type = ["FCFS", "RR", "SPN", "SRTN", "HRRN"]
cmb_scheduling_type = ttk.Combobox(input_frame, state="readonly", values=opt_scheduling_type, width=8)
cmb_scheduling_type.current(0)
cmb_scheduling_type.grid(column = 2, row = 0, padx = 10, pady = 10)

# TIMEQUANTUM
lb1_width = Label(input_frame, text="TIMEQUANTUM", width=12)
lb1_width.grid(column = 3, row = 0, padx = 10, pady = 10)

txt = Text(input_frame, width=10, height=1)
txt.grid(column = 4, row = 0, padx = 10, pady = 10)

# P CORE ADD BUTTON
btn_processorP_add = Button(input_frame, padx=5, pady=5, width=10, text="ADD P CORE")
btn_processorP_add.grid(column = 5, row = 0, padx = 10, pady = 10)

# E CORE ADD BUTTON
btn_processorE_add = Button(input_frame, padx=5, pady=5, width=10, text="ADD E CORE")
btn_processorE_add.grid(column = 6, row = 0, padx = 10, pady = 10)

# CORE DELETE BUTTON
btn_processor_delete = Button(input_frame, padx=5, pady=5, width=11, text="CORE DELETE")
btn_processor_delete.grid(column = 7, row = 0, padx = 10, pady = 10)

# # P CORE  옵션
# lb1_width = Label(input_frame, text="P", width=15)
# lb1_width.grid(column = 3, row = 0, padx = 10, pady = 10)
#
# opt_width = ["0", "1", "2", "3", "4"]
# cmb_width = ttk.Combobox(input_frame, state="readonly", values=opt_width, width=8)
# cmb_width.current(0)
# cmb_width.grid(column = 4, row = 0, padx = 10, pady = 10)
#
# # E CORE  옵션
# lb1_width = Label(input_frame, text="E", width=15)
# lb1_width.grid(column = 5, row = 0, padx = 10, pady = 10)
#
# opt_width = ["0", "1", "2", "3", "4"]
# cmb_width = ttk.Combobox(input_frame, state="readonly", values=opt_width, width=8)
# cmb_width.current(0)
# cmb_width.grid(column = 6, row = 0, padx = 10, pady = 10)

# PROCESS ADD BUTTON
btn_process_add = Button(input_frame, padx=5, pady=5, width=5, text="ADD")
btn_process_add.grid(column = 8, row = 0, padx = 10, pady = 10)

# PROCESS DELETE BUTTON
btn_process_delete = Button(input_frame, padx=5, pady=5, width=5, text="DELETE")
btn_process_delete.grid(column = 9, row = 0, padx = 10, pady = 10)

# RUN BUTTON
btn_run = Button(input_frame, padx=5, pady=5, width=5, text="RUN", bg="yellow")
btn_run.grid(column = 10, row = 0, padx = 10, pady = 10)

root.mainloop()
