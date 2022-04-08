from tkinter import *
import tkinter.ttk as ttk
from tkinter.colorchooser import *

root = Tk()
root.title("Hansongyi")
root.geometry("1040x600")
root.option_add("*Font", "맑은고딕 9")
root.resizable(False, False)
root.configure(bg="lavender")

file_frame = Frame(root)
file_frame.pack()

# lab_team_project
lab_team_project = Label(root, bg="lavender")
lab_team_project.config(text="운영체제 3조 이세희 이도형 조경우 한송이")
lab_team_project.pack(side="top", anchor="sw")

# lab_topic
lab_topic = Label(root, bg="lavender")
lab_topic.config(text="Scheduling setting", font="맑은고딕 20 bold")
lab_topic.pack()

# INPUT 프레임
input_frame = LabelFrame(root, bg="azure")
input_frame.pack()

# PROCESS_ROOT 프레임
process_root_frame = LabelFrame(root, width = 500, height = 330, bg = "lavender blush")
process_root_frame.pack(side="top", fill = BOTH, expand = 1)
# process_root_canvas_frame = LabelFrame(root, width = 500, height = 330)
# process_root_canvas_frame.pack(side="top", fill = BOTH, expand = 1)
#
# # PROCESS 스크롤바
# canvas = Canvas(process_root_canvas_frame)
# canvas.pack(side = LEFT, fill = BOTH, expand = 1)
#
# scrollbar = Scrollbar(process_root_canvas_frame, orient = VERTICAL, command = canvas.yview)
# scrollbar.pack(side = RIGHT, fill = Y)
#
# canvas.configure(yscrollcommand = scrollbar.set)
# canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
#
# process_root_frame = LabelFrame(canvas)
# canvas.create_window((0, 0), window = process_root_frame, anchor = "nw")
#
# for pr in range(15):
#     Label(process_root_frame, text = ("Process", pr+1)).grid(column = 0, row = pr, padx=10, pady=10)

# PROCESSOR_ROOT 프레임
processor_root_frame = LabelFrame(root, width = 500, height = 220, bg = "misty rose")
processor_root_frame.pack(side="top", fill = BOTH, expand = 1)

# SCHEDULING TYPE 옵션
lab_scheduling_type = Label(input_frame, text="SCHEDULING TYPE", width=15, bg="azure")
lab_scheduling_type.grid(column = 1, row = 0, padx = 10, pady = 10)

opt_scheduling_type = ["FCFS", "RR", "SPN", "SRTN", "HRRN"]

cmb_scheduling_type = ttk.Combobox(input_frame, state="readonly", values=opt_scheduling_type, width=8)
cmb_scheduling_type.current(0)
cmb_scheduling_type.grid(column = 2, row = 0, padx = 10, pady = 10)

# TIMEQUANTUM
lb1_width = Label(input_frame, text="TIMEQUANTUM", width=12, bg="azure")
lb1_width.grid(column = 3, row = 0, padx = 10, pady = 10)

txt = Text(input_frame, width=10, height=1)
txt.grid(column = 4, row = 0, padx = 10, pady = 10)

# core
p_core = 0
e_core = 0
core = []
# add p core
def add_p_core():
    global p_core
    global e_core
    global core
    if p_core + e_core < 4:
        # PROCESSOR 프레임
        core.append('p')
        processor_frame = LabelFrame(processor_root_frame, height = 3, width = 950, bg = color[p_core + e_core + 4])
        processor_frame.pack(side = "top", padx = 3, pady = 3)

        # CORE 명
        CORE = Label(processor_frame, text="P CORE", width=10, bg = color[p_core + e_core + 4])
        CORE.grid(column = 1, row = p_core + e_core, padx = 2, pady = 4)
        p_core += 1
        
# add e core
def add_e_core():
    global p_core
    global e_core
    global core
    if p_core + e_core < 4:
        # PROCESSOR 프레임
        core.append('e')
        processor_frame = LabelFrame(processor_root_frame, height = 3, width = 950, bg = color[p_core + e_core + 4])
        processor_frame.pack(side = "top", padx = 3, pady = 3)
        
        # CORE 명
        CORE = Label(processor_frame, text="E CORE", width=10, bg = color[p_core + e_core + 4])
        CORE.grid(column = 1, row = p_core + e_core, padx = 2, pady = 4)
        e_core += 1

# delete core
def delete_core():
    global p_core
    global e_core
    global core
    if p_core + e_core > 0:
        processor_root_frame.pack_slaves().pop().destroy()
        if core.pop == 'p':
            p_core -= 1
        else:
            e_core -= 1

# P CORE ADD BUTTON
btn_processorP_add = Button(input_frame, padx=5, pady=5, width=10, text="ADD P CORE", bg="azure")
btn_processorP_add.grid(column = 5, row = 0, padx = 10, pady = 10)
btn_processorP_add.config(command = add_p_core)

# E CORE ADD BUTTON
btn_processorE_add = Button(input_frame, padx=5, pady=5, width=10, text="ADD E CORE", bg="azure")
btn_processorE_add.grid(column = 6, row = 0, padx = 10, pady = 10)
btn_processorE_add.config(command = add_e_core)

# CORE DELETE BUTTON
btn_processor_delete = Button(input_frame, padx=5, pady=5, width=11, text="CORE DELETE", bg="azure")
btn_processor_delete.grid(column = 7, row = 0, padx = 10, pady = 10)
btn_processor_delete.config(command = delete_core)

# process
process = 0
arrival_time = []
burst_time = []
color = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream']

# add process
def add_process():
    global process
    global color
    if process < 15:
        # PROCESS 프레임
        process_frame = LabelFrame(process_root_frame, height = 2, width = 950, bg = color[process])
        process_frame.pack()
        
        # PROCESS 이름
        PROCESS = Label(process_frame, text=("P", process), width=10, bg = color[process])
        PROCESS.grid(column = 1, row = 0)

        # Arrival Time
        ARRIVAL_TIME = Label(process_frame, text="Arrival Time", width=12, bg = color[process])
        ARRIVAL_TIME.grid(column=2, row=0, padx=10, pady=10)
        TXT_ARRIVAL_TIME = Text(process_frame, width=10, height=1)
        TXT_ARRIVAL_TIME.grid(column=3, row=0, padx=10, pady=10)

        # Burst Time
        BURST_TIME = Label(process_frame, text="Burst Time", width=12, bg = color[process])
        BURST_TIME.grid(column=4, row=0, padx=10, pady=10)
        TXT_BURST_TIME = Text(process_frame, width=10, height=1)
        TXT_BURST_TIME.grid(column=5, row=0, padx=10, pady=10)

        process += 1

# delete process
def delete_process():
    global process
    if process > 0:
        process_root_frame.pack_slaves().pop().destroy()
        process -= 1

# PROCESS ADD BUTTON
btn_process_add = Button(input_frame, padx=5, pady=5, width=5, text="ADD", bg="azure")
btn_process_add.grid(column = 8, row = 0, padx = 10, pady = 10)
btn_process_add.config(command = add_process)

# PROCESS DELETE BUTTON
btn_process_delete = Button(input_frame, padx=5, pady=5, width=5, text="DELETE", bg="azure")
btn_process_delete.grid(column = 9, row = 0, padx = 10, pady = 10)
btn_process_delete.config(command = delete_process)

# RUN BUTTON
btn_run = Button(input_frame, padx=5, pady=5, width=5, text="RUN", bg="yellow")
btn_run.grid(column = 10, row = 0, padx = 10, pady = 10)

root.mainloop()
