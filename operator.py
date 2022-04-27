from locale import normalize
from pickle import FALSE
import FCFS
import pprint
import RR
import SPN
from time_calculator import turnaround_time  #이쁘게 출력하기 위한 (필요 없음)


def operator(gantt_type, scheduling_type, tq, at, bt):

    processor_number = len(gantt_type)    # Processor(Core) 개수
    
    while True :
        #input section
        power_used = 0  # 전력 소모량
        scheduling_type= -1 # 스케줄링 종류 (default : -1, FCFS : 1, RR : 2 ...) 
        
        '''
        turn_around_time = []
        waiting_time = []
        normalize_time = []
        '''
        #FCFS input and output 
        if(scheduling_type == "FCFS"):
            gantt_chart, power_used,turn_around_time,waiting_time,normalize_time = FCFS.fcfs(at, bt, processor_number, gantt_type)


        #Round Robin input and output (at, bt, pn, time_quantum, gt)
        if(scheduling_type == "RR"):
            gantt_chart, power_used,turn_around_time,waiting_time,normalize_time = RR.rr(at, bt, processor_number, 2, gantt_type)
        #time_quantum = 2 임의 설정 원하면 매개 변수 안 2를 변경


        #SPN input and out
        if(scheduling_type == "SPN"):
            gantt_chart, power_used,turn_around_time,waiting_time,normalize_time = SPN.spn(at, bt, processor_number, gantt_type)
        

        print("------------------------------------------------")
        print(gantt_chart, sep='\n')  #gantt print \n 
        print()
        print("Power Used : ", power_used)
        print("Turn around Time: ",turn_around_time)
        print("Waiting Time: ",waiting_time)
        print("Nomalize Time: ",normalize_time)
        print("------------------------------------------------")




#쓰레기 
'''    
def get_info(rr):
    # 도착 시간 입력
    arrival_time = list(map(int, input("Arrival Time : ").split()))
    
    # 실행 시간 입력
    burst_time = list(map(int, input("Burst Time :").split()))
    
    # Round-Robin일 때 Time-Quantum 입력 받음
    if rr == True :
        time_quantum = int(input("Time Quantum : "))
    return arrival_time, burst_time
        

def get_core(pn, gt) :
    core_type = input("Core Type : ")
    if core_type == 'P' :
        pn += 1
        gt.append('P')
    elif core_type == 'E' :
        pn += 1
        gt.append('E')
    return pn, gt
'''   



