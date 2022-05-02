from re import A
from threading import Timer
import col_gantt
import time_calculator
import copy

def hrrn(at, bt, pn, gantt_default) :  
    bt_copy = copy.deepcopy(bt)
    ready_queue = []            # 레디 큐
    line = [None] * len(at)     # 라인 리스트 (연속적인 입력을 위한 기억 리스트)
    timer = 0                   # 타이머
    end_time =[None] * len(at)  #end_time

    gantt = [["" for j in range(sum(bt)+10)] for j in range(pn)]     #make empty gantt 2 dimensional list   
    power_used = 0
    at_rr = []                  #SPN 추가 2차원 배열 (  [p1(at),p1(rr)] , 저장 ) 
    response_ratio = [0] * len(at)         #Response Ratio
    wtime = [0] * len(at)#NEW

    
    for i in range(pn) :
        gantt[i][0] = gantt_default[i]  # 간트 차트 초기값 'P','E' 입력    
        
    while True :                # 무한 반복
        used_core = 0           # 전력이 소비된 프로세서
        
        if timer in at :        # Arrival_Time -> Ready_Queue
            at_rr.append([at.index(timer),bt[at.index(timer)]]) #해당하는 ArriveTime process 저장 
            ready_queue.append(at.index(timer))  #ready에 정렬된 값을 넣는다.
 
        for processor_n in range(pn) :  # Processor(Core) -> 0부터 시작
            
            
            if processor_n in line  :      # 만약 라인 리스트에 n번째 프로세서가 잡히면

                 # 프로세스 추출
                process_num = line.index(processor_n)    
                
                if gantt[processor_n][0] == 'P' :
                    bt[process_num] -= 2                # 실행 시간 -2 (P)
                    power_used += 3                     # 3W (P)
                    used_core += 1  # 전력 소비
                    if bt[process_num] <= 0 :       # 만약 실행시간이 0이하 (P일 때 -1도 될수 있으니)
                        line[process_num] = 'None'  # 라인큐에서 나가리
                        end_time[process_num] = timer + 1
                    ready_queue = []                                    #ready 정렬해서 다시 받기 위해서 초기화 
                    for x, y in at_rr :
                        response_ratio[x] = (wtime[x] + bt[x]) / bt[x]
                        y = response_ratio[x]
                    for i in at_rr :
                        ready_queue.append(i[0])
                    at_rr.sort(key=lambda x: (x[1], x[0]))              #burst 적은 값으로 정렬한 후 (오름차순) 

                
                else : 
                    bt[process_num] -= 1                # 실행 시간 -1 (E)
                    power_used += 1                     # 1W (E)
                    used_core += 1  # 전력 소비
                    if bt[process_num] <= 0 :       # 만약 실행시간이 0이하 (P일 때 -1도 될수 있으니)
                        line[process_num] = 'None'  # 라인큐에서 나가리
                        end_time[process_num] = timer + 1
                    ready_queue = []                                    #ready 정렬해서 다시 받기 위해서 초기화 
                    for x, y in at_rr :
                        response_ratio[x] = (wtime[x] + bt[x]) / bt[x]
                        y = response_ratio[x]
                    for i in at_rr :
                        ready_queue.append(i[0])
                    at_rr.sort(key=lambda x: (x[1], x[0]))              #burst 적은 값으로 정렬한 후 (오름차순) 
                
                gantt[processor_n][timer+1] = col_gantt.colors(process_num)   # 간트에 집어 넣음
                
                
            elif len(ready_queue) != 0 :        # 레디큐가 안비워져 있으면 && line에 잡히는 것이 없다면
                process_num = ready_queue.pop(0) # 첫번째 값을 꺼내고 삭제한다.
                at_rr.pop(0)                     # ready Q와 같은 상태를 맞춰주기 위해 똑같이 삭제
                
                if gantt[processor_n][0] == 'P' :
                    bt[process_num] -= 2                # 실행 시간 -2 (P)
                    power_used += 3                     # 3W (P)
                    used_core += 1  # 전력 소비
                
                else : 
                    bt[process_num] -= 1                # 실행 시간 -1 (E)
                    power_used += 1                     # 1W (E)
                    used_core += 1  # 전력 소비
                
                gantt[processor_n][timer+1] = col_gantt.colors(process_num)   # 간트에 집어 넣음


                if bt[process_num] > 0 :
                    line[process_num] = processor_n  #해당 번째 processor를 다음에도 사용하겠습니다.
                else :
                    end_time[process_num] = timer + 1 
                
            else :      # 빈 것 -> 흰 것
                gantt[processor_n][timer+1] = 'White'

            power_used += (0.1*(pn-used_core))  # 대기 전력
            
        if max(bt) <= 0 :
            break
        

        for i in ready_queue :#NEW
            wtime[i] += 1 #NEW  
            print(i, "번 Process : ", wtime[i])
            
        timer += 1

    ttime = time_calculator.turnaround_time(at,end_time)
    ntime = time_calculator.normalized_tt(ttime, bt_copy)


    return gantt, power_used,ttime,wtime,ntime












'''

from re import A
import col_gantt
import time_calculator
import copy

def hrrn(at, bt, pn, gantt_default) :  
    bt_copy = copy.deepcopy(bt)
    ready_queue = []            # 레디 큐
    line = [None] * len(at)     # 라인 리스트 (연속적인 입력을 위한 기억 리스트)
    timer = 0                   # 타이머
    end_time =[None] * len(at)  #end_time

    gantt = [["" for j in range(sum(bt)+10)] for j in range(pn)]     #make empty gantt 2 dimensional list   
    power_used = 0
    at_rr = []                  #SPN 추가 2차원 배열 (  [p1(at),p1(rr)] , 저장 ) 
    response_ratio = [None] * len(at)         #Response Ratio
    wtime = [0] * len(at)#NEW

    
    for i in range(pn) :
        gantt[i][0] = gantt_default[i]  # 간트 차트 초기값 'P','E' 입력    
        
    while True :                # 무한 반복
        used_core = 0           # 전력이 소비된 프로세서
        
        if timer in at :        # Arrival_Time -> Ready_Queue
            
            ready_queue = []                                    #ready 정렬해서 다시 받기 위해서 초기화 
            at_rr.append([at.index(timer),bt[at.index(timer)]]) #해당하는 ArriveTime process 저장 
            for x, y in at_rr :
                response_ratio[x] = (wtime[x] + bt[x]) / bt[x]
                print(x,"번째 : ", wtime[x], " ", bt[x], " ", response_ratio)
                y = response_ratio[x]
            at_rr.sort(key=lambda x: (x[1], x[0]), reverse=True)#burst 적은 값으로 정렬한 후 (오름차순) 

            for i in at_rr:
                ready_queue.append(i[0])  #ready에 정렬된 값을 넣는다.

        for processor_n in range(pn) :  # Processor(Core) -> 0부터 시작
            
            
            if processor_n in line  :      # 만약 라인 리스트에 n번째 프로세서가 잡히면

                 # 프로세스 추출
                process_num = line.index(processor_n)    
                
                if gantt[processor_n][0] == 'P' :
                    bt[process_num] -= 2                # 실행 시간 -2 (P)
                    power_used += 3                     # 3W (P)
                    used_core += 1  # 전력 소비
                    if bt[process_num] <= 0 :       # 만약 실행시간이 0이하 (P일 때 -1도 될수 있으니)
                        line[process_num] = 'None'  # 라인큐에서 나가리
                        end_time[process_num] = timer + 1
                
                else : 
                    bt[process_num] -= 1                # 실행 시간 -1 (E)
                    power_used += 1                     # 1W (E)
                    used_core += 1  # 전력 소비
                    if bt[process_num] <= 0 :       # 만약 실행시간이 0이하 (P일 때 -1도 될수 있으니)
                        line[process_num] = 'None'  # 라인큐에서 나가리
                        end_time[process_num] = timer + 1
                
                gantt[processor_n][timer+1] = col_gantt.colors(process_num)   # 간트에 집어 넣음
                
                
            elif len(ready_queue) != 0 :        # 레디큐가 안비워져 있으면 && line에 잡히는 것이 없다면
                process_num = ready_queue.pop(0) # 첫번째 값을 꺼내고 삭제한다.
                at_rr.pop(0)                     # ready Q와 같은 상태를 맞춰주기 위해 똑같이 삭제
                
                if gantt[processor_n][0] == 'P' :
                    bt[process_num] -= 2                # 실행 시간 -2 (P)
                    power_used += 3                     # 3W (P)
                    used_core += 1  # 전력 소비
                
                else : 
                    bt[process_num] -= 1                # 실행 시간 -1 (E)
                    power_used += 1                     # 1W (E)
                    used_core += 1  # 전력 소비
                
                gantt[processor_n][timer+1] = col_gantt.colors(process_num)   # 간트에 집어 넣음


                if bt[process_num] > 0 :
                    line[process_num] = processor_n  #해당 번째 processor를 다음에도 사용하겠습니다.
                else :
                    end_time[process_num] = timer + 1 
                
            else :      # 빈 것 -> 흰 것
                gantt[processor_n][timer+1] = 'White'

            power_used += (0.1*(pn-used_core))  # 대기 전력
            
        if max(bt) <= 0 :
            break
        

        for i in ready_queue :#NEW
            wtime[i] += 1#NEW
            
        timer += 1

    ttime = time_calculator.turnaround_time(at,end_time)
    ntime = time_calculator.normalized_tt(ttime, bt_copy)


    return gantt, power_used,ttime,wtime,ntime




'''