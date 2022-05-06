import col_gantt
import time_calculator
import copy


def srtn(at, bt, pn, gantt_default):
    bt_copy = copy.deepcopy(bt)
    timer = 0  # 타이머
    end_time = [None] * len(at)  # end_time
    gantt = [["" for j in range(sum(bt)+10)] for j in range(pn)]  # make empty gantt 2 dimensional list
    power_used = 0
    at_bt = []                  #SPN 추가 2차원 배열 (  [p1(at),p1(bt)] , 저장 ) 
    tmp_at_bt = []
    wtime = [0] * len(at)#NEW

    for i in range(pn):
        gantt[i][0] = gantt_default[i]  # 간트 차트 초기값 'P','E' 입력

    while True:  # 무한 반복
        used_core = 0  # 전력이 소비된 프로세서
        
        while len(tmp_at_bt) != 0 :
            at_bt.append(tmp_at_bt.pop())
        
        if timer in at:  # Arrival_Time -> Ready_Queue
            at_bt.append([at.index(timer),bt[at.index(timer)]]) #해당하는 ArriveTime process 저장 
            at_bt.sort(key=lambda x: (x[1], x[0]))              #burst 적은 값으로 정렬한 후 (오름차순) 

        for processor_n in range(pn):  # Processor(Core) -> 0부터 시작
            gantt[processor_n].append('')
            if len(at_bt) != 0:  # 레디큐가 안비워져 있으면 
                process_num = at_bt[0][0] 
                if gantt[processor_n][0] == 'P':
                    at_bt[0][1] -= 2  # 실행 시간 -2 (P)
                    bt[process_num] -= 2
                    power_used += 3  # 3W (P)
                    used_core += 1  # 전력 소비

                else:
                    at_bt[0][1] -= 1  # 실행 시간 -1 (E)
                    bt[process_num] -= 1
                    power_used += 1  # 1W (E)
                    used_core += 1  # 전력 소비

                gantt[processor_n][timer + 1] = col_gantt.colors(process_num)  # 간트에 집어 넣음

                if bt[process_num] <= 0: 
                    end_time[process_num] = timer + 1 
                    at_bt.pop(0)
                else :
                    wtime[process_num] -= 1 
                    tmp_at_bt.append(at_bt.pop(0))
            else:  # 빈 것 -> 흰 것
                gantt[processor_n][timer + 1] = 'White'

            power_used += (0.1 * (pn - used_core))  # 대기 전력

        if max(bt) <= 0:  #bt 가  모두 0일때 
            break

        for i in at_bt :
            k = i[0]
            wtime[k] += 1

        timer += 1

    ttime = time_calculator.turnaround_time(at, end_time)
    ntime = time_calculator.normalized_tt(ttime, bt_copy)

    # remvoe '' element
    for i in range(len(gantt)):            # 세로 크기
        for j in range(len(gantt[i])):     # 가로 크기
            gantt[i] = ' '.join(gantt[i]).split() 

    return gantt, power_used, ttime, wtime, ntime