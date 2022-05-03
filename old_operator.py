from locale import normalize
import FCFS
import pprint
import RR
import SRTN
import SPN 
import HRRN
import WTT
from time_calculator import turnaround_time  #이쁘게 출력하기 위한 (필요 없음)


def main():

    
    processor_number = 0    # Processor(Core) 개수
    gantt_type = []         # P, E코어
    
    while True :
        #input section
        status = -1     # 상태 (default : -1, add: 0, delete : 1, add Core : 2)
        power_used = 0  # 전력 소모량
        scheduling = -1 # 스케줄링 종류 (default : -1, FCFS : 1, RR : 2 ...) 
        round_robin = False;    # Round Robin 여부
        turn_around_time = 0
        waiting_time = 0
        normalize_time=0

    
        status = int(input("현재 상태 : "))  

        if status == 0 :  
            at, bt = get_info(round_robin)  
            
        elif status == 2 :
            processor_number, gt = get_core(processor_number, gantt_type)
            continue
    

        #FCFS input and output 
        #gantt_chart, power_used,turn_around_time,waiting_time,normalize_time = FCFS.fcfs(at, bt, processor_number, gt)


        #Round Robin input and output
        #gantt_chart, power_used,turn_around_time,waiting_time,normalize_time = RR.rr(at, bt, processor_number,3, gt)

        #SPN
        #gantt_chart, power_used,turn_around_time,waiting_time,normalize_time = SPN.spn(at, bt, processor_number, gt)

        #SRTN input and output 
        #gantt_chart, power_used,turn_around_time,waiting_time,normalize_time = SRTN.srtn(at, bt, processor_number, gt)

        #HRRN
        #gantt_chart, power_used,turn_around_time,waiting_time,normalize_time = HRRN.hrrn(at, bt, processor_number, gt)


        #new WTT
        gantt_chart, power_used,turn_around_time,waiting_time,normalize_time = WTT.wtt(at, bt, processor_number,3, gt)



        print("------------------------------------------------")
        print(*gantt_chart, sep='\n')  #gantt print \n 
        print()
        print("Power Used : ", power_used)
        print("Turn around Time: ",turn_around_time)
        print("Waiting Time: ",waiting_time)
        print("Nomalize Time: ",normalize_time)

        print("------------------------------------------------")
    
def get_info(rr):
    # 도착 시간 입력
    arrival_time = list(map(int, input("Arrival Time : ").split()))
    
    # 실행 시간 입력
    burst_time = list(map(int, input("Burst Time :").split()))
    
    if rr == True : # Round-Robin일 때 Time-Quantum 입력 받음
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
        
if __name__ == "__main__" :
    main()

