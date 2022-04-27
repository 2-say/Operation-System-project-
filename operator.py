from locale import normalize
import FCFS
import pprint
import RR
import SPN
from time_calculator import turnaround_time  #이쁘게 출력하기 위한 (필요 없음)


#사용법##############################
#처음 2를 입력해서 core를 추가시킨다.
#4개 이하까지 추가 후 0을 입력해 at , bt를 입력받는다.
#입력 양식 예) 1 2 3 4 5 (띄어쓰기 구분)
#SPN , FCFS , RR 사용하려면  49 , 53, 57 줄 주석 해제 후 사용 (하나만) 


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


        #Round Robin input and output (at, bt, pn, time_quantum, gt)
        #gantt_chart, power_used,turn_around_time,waiting_time,normalize_time = RR.rr(at, bt, processor_number, 2, gt)
        #time_quantum = 2 임의 설정 원하면 매개 변수 안 2를 변경


        #SPN input and out
        #gantt_chart, power_used,turn_around_time,waiting_time,normalize_time = SPN.spn(at, bt, processor_number, gt)
        

        print("------------------------------------------------")
        print(gantt_chart, sep='\n')  #gantt print \n 
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
        
if __name__ == "__main__" :
    main()


