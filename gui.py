from tkinter import *
import tkinter.ttk as ttk
import team_operator
import time

# Colors ###########################
color1 = "#FFFFFF"
bg_color = "#ECEFF1";
color = ['#FFCDD2', '#F8BBD0', '#D1C4E9', '#C5CAE9', 'old lace', 'floral white',
         'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
         'navajo white', 'lemon chiffon', 'mint cream', bg_color]
color_dic = {"White" : 15, "p1_color" : 0, "p2_color" : 1, "p3_color" : 2, "p4_color" : 3,
                 "p5_color" : 4, "p6_color" : 5, "p7_color" : 6, "p8_color" : 7, "p9_color" : 8, "p10_color" : 9,
                 "p11_color" : 10, "p13_color" : 11, "p11_color" : 12, "p11_color" : 13, "p11_color" : 14}
####################################

# Variables ########################
core = []
p_core = 0
e_core = 0
process = 0
scheduling_type = ""
time_quantum = 0
process_arrival_time = []
process_burst_time = []
####################################

# Function #########################
# Add Process
def add_process():
    global process
    global color
    if process < 15:
        # Frame To Be Add
        add_frame = LabelFrame(process_frame, bg = bg_color, relief="flat")
        add_frame.pack(side="top", fill="both")

        # Process name
        lab_add = Label(add_frame, text=("P", process + 1), bg = bg_color, width=10, padx=15)
        lab_add.config(font="맑은고딕 8 bold")
        lab_add.grid(column=0, row=0, padx=15, pady=10)

        # Arrival Time
        txt_add = Text(add_frame, width=15, height=1.5, padx=5)
        txt_add.insert(INSERT, "0")
        txt_add.grid(column=1, row=0, padx=15, pady=10)

        # Burst Time
        txt_add = Text(add_frame, width=15, height=1.5, padx=5)
        txt_add.insert(INSERT, "0")
        txt_add.grid(column=2, row=0, padx=15, pady=10)

        # Waiting Time
        lab_add = Label(add_frame, text="", bg = bg_color, width=1, padx=50)
        lab_add.config(font="맑은고딕 8 bold")
        lab_add.grid(column=6, row=0, padx=15, pady=10)

        # Turnarround Time
        lab_add = Label(add_frame, text="",  bg = bg_color, width=10, padx=50)
        lab_add.config(font="맑은고딕 8 bold")
        lab_add.grid(column=7, row=0, padx=15, pady=10)

        # Normalized Turnarround Time
        lab_add = Label(add_frame, text="",  bg = bg_color, width=10, padx=50)
        lab_add.config(font="맑은고딕 8 bold")
        lab_add.grid(column=8, row=0, padx=15, pady=10)

        process += 1

# Delete Process
def delete_process():
    global process
    if process > 0:
        process_frame.pack_slaves().pop().destroy()
        process -= 1

# Add P Core
def add_p_core():
    global p_core
    global e_core
    global core
    if p_core + e_core < 4:
        core.append('P')
        p_core += 1

        # Processor Frame
        add_frame = LabelFrame(core_frame, height=3, width=900, bg=bg_color, relief="flat")
        add_frame.pack(side="top", fill="both")

        # Core Type
        lab_add = Label(add_frame, text="P CORE", height = 3, width=10, bg=bg_color)
        lab_add.config(font="맑은고딕 8 bold")
        lab_add.grid(column=1, row=0, padx=2)

        # Gantt Frame
        gantt_frame = Frame(add_frame, height=40,width=900, bg=bg_color)
        gantt_frame.grid(column=2, row=0, padx=10)

# Add E Core
def add_e_core():
    global p_core
    global e_core
    global core
    if p_core + e_core < 4:
        core.append('E')
        e_core += 1

        # Processor Frame
        add_frame = LabelFrame(core_frame, bg= bg_color,  relief="flat")
        add_frame.pack(side="top", fill="both")

        # Core Type
        CORE = Label(add_frame, text="E CORE", height = 2, width=10, bg=bg_color)
        CORE.config(font="맑은고딕 8 bold")
        CORE.grid(column=1, row=0, padx=2)

        # Gantt Frame
        gantt_frame = Frame(add_frame,height=40, width=900, bg=bg_color)
        gantt_frame.grid(column=2, row=0, padx=10)

# Delete Core
def delete_core():
    global p_core
    global e_core
    global core
    if p_core + e_core > 0:
        core_frame.pack_slaves().pop().destroy()
        c_delete = core.pop()
        if c_delete == 'P':
            p_core -= 1
        else:
            e_core -= 1

    else:
        # for k in processor_canvas_frame.pack_slaves().pop(0).grid_slaves().pop(0).grid_slaves():
        #     k.destroy()
        core_frame.pack_slaves().pop(0).grid_slaves().pop(0).destroy()
        core_frame.pack_slaves().pop(1).grid_slaves().pop(0).destroy()
        tmp = Frame(readyQ_root_frame, height=40, width=900, bg=bg_color)
        tmp.grid(column=2, row=0, padx=10)
        tmp = Frame(time_root_frame, height=40, width=900, bg=bg_color)
        tmp.grid(column=2, row=0, padx=10)

# Update ------
def update_process(turn_around_time, waiting_time, normalize_time):
    for i in range(process):
        update_frame = process_frame.pack_slaves().pop(i)
        update_frame.grid_slaves().pop(2).configure(text=round(waiting_time[i], 2))
        update_frame.grid_slaves().pop(1).configure(text=round(turn_around_time[i], 2))
        update_frame.grid_slaves().pop(0).configure(text=round(normalize_time[i], 2))

def update_label(gantt_chart, i):
    for j in range(len(gantt_chart)):
        update_frame = core_frame.pack_slaves().pop(j+2).grid_slaves().pop(0)
        if color_dic[gantt_chart[j][i]] + 1 < 16:
            lab_update = Label(update_frame, text = "P"+str(color_dic[gantt_chart[j][i]]+1), height = 2, width = 4,
                               bg = color[int(color_dic[gantt_chart[j][i]])], font = "맑은고딕 11 bold")
        else:
            lab_update = Label(update_frame, height = 2, width = 4, bg = color[int(color_dic[gantt_chart[j][i]])], font = "맑은고딕 11 bold")
        lab_update.grid(column=i, row=0, padx=3, pady=3)

def update_readyQ(readyQ, num):
    clear_readyQ()
    for i in range(len(readyQ[num])):
        update_frame = core_frame.pack_slaves().pop(0).grid_slaves().pop(0)
        lab_update = Label(update_frame, text="P"+str(readyQ[num][i]+1), height=1, width=4, font="맑은고딕 11 bold",
                           bg=color[readyQ[num][i]])
        lab_update.grid(column=i + 1, row=0, padx=3, pady=3)

def update_time(n):
    for i in range(n-1):
        update_frame = core_frame.pack_slaves().pop(1).grid_slaves().pop(0)
        lab_update = Label(update_frame, text = str(i+1), height=1, width=4, font="맑은고딕 11 bold", bg= bg_color)
        lab_update.grid(column=i+1, row=0, padx=3, pady=3)

def update_core(gantt_chart, readyQ):
    update_time(len(gantt_chart[0]))
    for i in range(1, len(gantt_chart[0])):
        update_label(gantt_chart, i)
        update_readyQ(readyQ, i)
        root.update()
        time.sleep(0.5)

def update_power_used(power_used):
    update_frame = core_frame.pack_slaves().pop(0).grid_slaves().pop(2)
    update_frame.grid_slaves().pop(0).configure(text=str(round(power_used, 2))+'W')
# -------------

def clear_power_used():
    update_frame = core_frame.pack_slaves().pop(0).grid_slaves().pop(2)
    update_frame.grid_slaves().pop(0).configure(text='')

def clear_core(size):
    clear_power_used()
    for j in range(size):
        delete_chart = core_frame.pack_slaves().pop(j + 2).grid_slaves().pop(0)
        for k in delete_chart.grid_slaves():
            k.destroy()

def clear_readyQ():
    core_frame.pack_slaves().pop(0).grid_slaves().pop(0).destroy()
    tmp = Frame(readyQ_root_frame, height=40, width=700, bg=bg_color)
    tmp.grid(column=2, row=0, padx=10)

# Clear Time Labels
def clear_time():
    core_frame.pack_slaves().pop(1).grid_slaves().pop(0).destroy()
    tmp = Frame(time_root_frame, height=40, width=900, bg=bg_color)
    tmp.grid(column=2, row=0, padx=10)

# Clear Variables
def clear_variables():
    global time_quantum
    global process_arrival_time
    global process_burst_time
    time_quantum = 0
    process_arrival_time.clear()
    process_burst_time.clear()

# Run
def run():
    clear_variables()
    global scheduling_type
    global time_quantum
    global process_arrival_time
    global process_burst_time
    global core
    global p_core
    global e_core

    scheduling_type = input_frame.grid_slaves().pop(9).get()
    time_quantum = int(input_frame.grid_slaves().pop(7).get(1.0, "end - 1c"))

    for i in range(process):
        get_frame = process_frame.pack_slaves().pop(i)
        process_arrival_time.append(int(get_frame.grid_slaves().pop(4).get(1.0, "end - 1c")))
        process_burst_time.append(int(get_frame.grid_slaves().pop(3).get(1.0, "end - 1c")))

    gantt_chart, power_used, turn_around_time, waiting_time, normalize_time, readyQ= \
        team_operator.operator(core, scheduling_type, time_quantum, process_arrival_time, process_burst_time)

    clear_core(len(gantt_chart))
    clear_time()

    update_process(turn_around_time, waiting_time, normalize_time)
    update_core(gantt_chart, readyQ)
    update_power_used(power_used)

# Clear All
def clear():
    global process
    global p_core
    global e_core
    clear_variables()

    num = process
    for i in range(num):
        delete_process()
    num = p_core + e_core
    for i in range(num):
        delete_core()
    delete_core()

def process_function(event):
    canvas_process.configure(scrollregion=canvas_process.bbox("all"), bg=bg_color)

def core_function(event):
    canvas_core.configure(scrollregion=canvas_core.bbox("all"), bg=bg_color)
####################################

####################################
# Window Frame
root = Tk()
root.title("Operation System")
root.geometry("1040x800")
root.option_add("*Font", "맑은고딕 9")
root.resizable(False, False)
root.configure(bg=color1)
####################################

####################################
# Team Info
lab_team_info = Label(root, bg=color1)
lab_team_info.config(text="운영체제 3e조 이세희 이도형 조경우 한송이", font="맑은고딕 10")
lab_team_info.pack(side="top", anchor="sw")
####################################

####################################
# Topic
lab_topic = Label(root, bg=color1)
lab_topic.config(text="Scheduling setting", font="맑은고딕 20 bold")
lab_topic.pack(pady=20)
####################################

####################################
# Input Frame
input_frame = Frame(root, bg=color1)
input_frame.pack(fill=BOTH, pady=10)

# Scheduling Type Option
lab_scheduling_type = Label(input_frame, text="SCHEDULING TYPE", width=15, bg=color1)
lab_scheduling_type.config(font="맑은고딕 10")
lab_scheduling_type.grid(column=1, row=0, padx=10, pady=10)

opt_scheduling_type = ["FCFS", "RR", "SPN", "SRTN", "HRRN", "WTQ"]

cmb_scheduling_type = ttk.Combobox(input_frame, state="readonly", values=opt_scheduling_type, width=8)
cmb_scheduling_type.current(0)
cmb_scheduling_type.grid(column=2, row=0, padx=10, pady=10)

# Time Quantum
lab_tq = Label(input_frame, text="TIMEQUANTUM", width=12, bg="#FFFFFF")
lab_tq.config(font="맑은고딕 10")
lab_tq.grid(column=3, row=0, padx=10, pady=10)

txt_tq = Text(input_frame, width=10, height=1)
txt_tq.insert(INSERT, "0")
txt_tq.grid(column=4, row=0, padx=10, pady=10)

# Process Add Button
btn_process_add = Button(input_frame, padx=5, pady=5, width=5, text="ADD", bg="#B2EBF2", relief="groove",
                         overrelief="solid", bd=0, activebackground="#B2EBF2")
btn_process_add.grid(column=5, row=0, padx=10, pady=10)
btn_process_add.config(command=add_process)

# Process Delete Button
btn_process_delete = Button(input_frame, padx=5, pady=5, width=5, text="DELETE", bg="#B2EBF2", relief="groove",
                            overrelief="solid", bd=0, activebackground="#B2EBF2")
btn_process_delete.grid(column=6, row=0, padx=10, pady=10)
btn_process_delete.config(command=delete_process)

# P Core Add Button
btn_Pcore_add = Button(input_frame, padx=5, pady=5, width=10, text="ADD P CORE", bg="#C5CAE9", relief="groove",
                            overrelief="solid", bd=0, activebackground="#C5CAE9")
btn_Pcore_add.grid(column=7, row=0, padx=10, pady=10)
btn_Pcore_add.config(command=add_p_core)

# E Core Add Button
btn_Ecore_add = Button(input_frame, padx=5, pady=5, width=10, text="ADD E CORE", bg="#C5CAE9", relief="groove",
                            overrelief="solid", bd=0, activebackground="#C5CAE9")
btn_Ecore_add.grid(column=8, row=0, padx=10, pady=10)
btn_Ecore_add.config(command=add_e_core)

# Core Delete Button
btn_core_delete = Button(input_frame, padx=5, pady=5, width=11, text="CORE DELETE", bg="#C5CAE9", relief="groove",
                              overrelief="solid", bd=0, activebackground="#C5CAE9")
btn_core_delete.grid(column=9, row=0, padx=10, pady=10)
btn_core_delete.config(command=delete_core)

# Run Button
btn_run = Button(input_frame, padx=5, pady=5, width=5, text="RUN", bg="#FFF9C4", relief="groove", overrelief="solid",
                 bd=0, activebackground="#FFF9C4")
btn_run.grid(column=10, row=0, padx=10, pady=10)
btn_run.config(command=run)

# Clear Button
btn_clear = Button(input_frame, padx=5, pady=5, width=5, text="CLEAR", bg="#FFCCBC", bd=0, activebackground="#FFCCBC")
btn_clear.grid(column=11, row=0, padx=10, pady=10)
btn_clear.config(command=clear)
####################################

####################################
# PROCESS_ROOT 프레임
process_root_frame = Frame(root, bg=bg_color, relief="flat")
process_root_frame.pack(side="top", fill="both")

# Process Info Frame
pif_font = "맑은고딕 9 bold"
pif_color = "#B0BEC5"
process_info_frame = LabelFrame(process_root_frame, bg=pif_color, font=pif_font)
process_info_frame.pack(side="top", fill="both")

lab_add = Label(process_info_frame, text="Process", width=15, bg=pif_color, font=pif_font)
lab_add.grid(column=0, row=0, padx=10, pady=10)

lab_add = Label(process_info_frame, text="Arrive Time", width=15, bg=pif_color, font=pif_font)
lab_add.grid(column=1, row=0, padx=10, pady=10)

lab_add = Label(process_info_frame, text="Burst Time", width=15, bg=pif_color, font=pif_font)
lab_add.grid(column=2, row=0, padx=10, pady=10)

lab_add = Label(process_info_frame, text="Waiting Time", width=20, bg=pif_color, font=pif_font)
lab_add.grid(column=3, row=0, padx=15, pady=10)

lab_add = Label(process_info_frame, text="Turnaround Time", width=20, bg=pif_color, font=pif_font)
lab_add.grid(column=4, row=0, padx=15, pady=10)

lab_add = Label(process_info_frame, text="Normalized Turnaround Time", width=30, bg=pif_color, font=pif_font)
lab_add.grid(column=5, row=0, padx=15, pady=10)

# Process Canvas 생성
canvas_process = Canvas(process_root_frame, bg=bg_color, width=1020)
process_frame = Frame(canvas_process, bg=bg_color)

# 세로 스크롤바 생성
scrollbar_process = Scrollbar(process_root_frame, orient="vertical", command=canvas_process.yview, width=20)
canvas_process.configure(yscrollcommand=scrollbar_process.set)

scrollbar_process.pack(side="right", fill="y")
canvas_process.pack(side="left")
canvas_process.create_window((0, 0), window=process_frame, anchor=NW, width = 1020)
process_frame.bind("<Configure>", process_function)
####################################

####################################
# PROCESSOR_ROOT 프레임
processor_root_frame = LabelFrame(root, bg=bg_color, bd =3)
processor_root_frame.pack(side="top", fill="both")

# Core Canvas
canvas_core = Canvas(processor_root_frame, bg=bg_color, width = 1000, height=500, bd =2)
core_frame = Frame(canvas_core, bg=bg_color)

# Scroll Bar
scrollbar_core = Scrollbar(processor_root_frame, orient="horizontal", command=canvas_core.xview, width = 20)
canvas_core.configure(xscrollcommand=scrollbar_core.set)

scrollbar_core.pack(side="bottom", fill="x")
canvas_core.pack(side="top")
canvas_core.create_window((0, 0), window=core_frame, anchor=NW)
core_frame.bind("<Configure>", core_function)

# ReadyQ Root Frame
readyQ_root_frame = LabelFrame(core_frame, height=3, width=900, bg=bg_color, relief="flat")
readyQ_root_frame.pack(side="top", fill="both")

# Power Used Frame
power_used = Frame(readyQ_root_frame,height=40, width=100, bg=bg_color)
power_used.grid(column=0, row=0, padx=10)

# Power Used Label
lab_power_used = Label(power_used, text="Power Used", width=10, bg=bg_color)
lab_power_used.config(font="맑은고딕 8 bold")
lab_power_used.grid(column=0, row=0, padx=10, pady=10)

lab_used_power = Label(power_used, text="", bg = bg_color, width=1, padx=50)
lab_used_power.config(font="맑은고딕 8 bold")
lab_used_power.grid(column=1, row=0, padx=15, pady=10)

# ReadyQ Label
readyQ = Label(readyQ_root_frame, text="Ready Queue", height=2, width=10, bg=bg_color)
readyQ.config(font="맑은고딕 8 bold")
readyQ.grid(column=1, row=0, padx=2)

# ReadyQ Frame
readyQ_frame = Frame(readyQ_root_frame, height=40, width=600, bg=bg_color)
readyQ_frame.grid(column=2, row=0, padx=10)

# Time Root Frame
time_root_frame = LabelFrame(core_frame, height=3, width=900, bg=bg_color, relief="flat")
time_root_frame.pack(side="top", fill="both")

sequence = Label(time_root_frame, text="Time", height=2, width=6, bg=bg_color)
sequence.config(font="맑은고딕 8 bold")
sequence.grid(column=0, row=0, padx=2)

time_0 = Label(time_root_frame, text="0", height=2, width=4, bg=bg_color)
time_0.config(font="맑은고딕 11 bold")
time_0.grid(column=1, row=0, padx=2)

# Time Frame
time_frame = Frame(time_root_frame,height=40, width=900, bg=bg_color)
time_frame.grid(column=2, row=0, padx=10)
####################################

root.mainloop()