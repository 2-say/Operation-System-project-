arrival_time = []   # arrival time is list [15]
burst_time = []     # burst time is list as well
gantt_chart = [None] * 100   # Gantt Chart

status = -1         # status : 0(add), 1(delete), -1(default)
process = 0         # process 0~14
#processor = 1       # processors 1~4
gantt_location = 0  # gantt_location 0~100
color = "White"

if status == 0 :    # add situation
    arrival_time[process] = input("Arrival Time : ")
    burst_time[process] = input("Burst Time : ")
    process += 1
    status = -1
    
elif status == 1 :  # delete situation (if can select process num.)
    del arrival_time[process-1]
    del burst_time[process-1]
    status = -1

fastest = min(arrival_time) # find fastest arrival time
location = arrival_time.find(fastest)    # fastest location

if  gantt_location >= fastest :
    for i in range(burst_time[location]) :
        gantt_chart[gantt_location] = color
        gantt_location += 1
        
else :
    gantt_chart[gantt_location] = "White"
    gantt_location += 1    
