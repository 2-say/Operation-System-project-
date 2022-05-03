import col_gantt
import time_calculator
import copy


def srtn(at, bt, pn, gantt_default):
    #bt_copy = copy.deepcopy(bt)
    ready_queue = []  # 레디 큐
    line = [None] * len(at)  # 라인 리스트 (연속적인 입력을 위한 기억 리스트)
    timer = 0  # 타이머
    end_time = [None] * len(at)  # end_time
    
    wtime = [0] * len(at)#NEW

    gantt = [["" for j in range(min(at))] for j in range(pn)]  # make empty gantt 2 dimensional list

    power_used = 0
    at_bt = []                  #SPN 추가 2차원 배열 (  [p1(at),p1(bt)] , 저장 ) 
    wtime = [0] * len(at)#NEW



    for i in range(pn):
        gantt[i][0] = gantt_default[i]  # 간트 차트 초기값 'P','E' 입력

    while True:  # 무한 반복
        used_core = 0  # 전력이 소비된 프로세서
        if timer in at:  # Arrival_Time -> Ready_Queue
            #ready_queue = []
            #ready_queue.append(at.index(timer))
            at_bt.append([at.index(timer),bt[at.index(timer)]]) #해당하는 ArriveTime process 저장 
            at_bt.sort(key=lambda x: (x[1], x[0]))              #burst 적은 값으로 정렬한 후 (오름차순) 


        for processor_n in range(pn):  # Processor(Core) -> 0부터 시작
            gantt[processor_n].append('')
            '''
            if processor_n in line:  # 만약 라인 리스트에 n번째 프로세서가 잡히면

                # 프로세스 추출
                process_num = line.index(processor_n)

                if gantt[processor_n][0] == 'P':
                    bt[process_num] -= 2  # 실행 시간 -2 (P)
                    power_used += 3  # 3W (P)
                    used_core += 1  # 전력 소비
                    if bt[process_num] <= 0:  # 만약 실행시간이 0이하 (P일 때 -1도 될수 있으니)
                        #line[process_num] = 'None'  # 라인큐에서 나가리
                        end_time[process_num] = timer + 1

                else:
                    bt[process_num] -= 1  # 실행 시간 -1 (E)
                    power_used += 1  # 1W (E)
                    used_core += 1  # 전력 소비
                    if bt[process_num] <= 0:  # 만약 실행시간이 0이하 (P일 때 -1도 될수 있으니)
                        #line[process_num] = 'None'  # 라인큐에서 나가리
                        end_time[process_num] = timer + 1

                gantt[processor_n][timer + 1] = col_gantt.colors(process_num)  # 간트에 집어 넣음

                '''
            if len(at_bt) != 0:  # 레디큐가 안비워져 있으면 && line에 잡히는 것이 없다면
                process_num = at_bt[0][0] # 첫번째 값을 꺼내고 삭제한다. 
                if gantt[processor_n][0] == 'P':
                    at_bt[0][1] -= 2  # 실행 시간 -2 (P)
                    power_used += 3  # 3W (P)
                    used_core += 1  # 전력 소비

                else:
                    at_bt[0][1] -= 1  # 실행 시간 -1 (E)
                    power_used += 1  # 1W (E)
                    used_core += 1  # 전력 소비

                gantt[processor_n][timer + 1] = col_gantt.colors(process_num)  # 간트에 집어 넣음

                if at_bt[0][1] <= 0:
                    end_time[process_num] = timer + 1
                    at_bt.pop(0)
                else :
                    wtime[process_num] -= 1

            else:  # 빈 것 -> 흰 것
                gantt[processor_n][timer + 1] = 'White'

            power_used += (0.1 * (pn - used_core))  # 대기 전력

        if max(at_bt[][1]) <= 0:  #bt 가  모두 0일때 
            break

        for i in at_bt[][0]
            wtime[i] += 1


        timer += 1

    ttime = time_calculator.turnaround_time(at, end_time)
    ntime = time_calculator.normalized_tt(ttime, bt_copy)


    # remvoe '' element

    for i in range(len(gantt)):            # 세로 크기
        for j in range(len(gantt[i])):     # 가로 크기
            gantt[i] = ' '.join(gantt[i]).split() 


    return gantt, power_used, ttime, wtime, ntime