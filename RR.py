import col_gantt
import time_calculator
import copy


def rr(at, bt, pn, time_quantum, gantt_default):
    bt_copy = copy.deepcopy(bt)  # waiting , ntt를 계산하기 위해 원복 복사
    ready_queue = []  # 레디 큐
    line = [None] * len(at)  # 라인 리스트 (연속적인 입력을 위한 기억 리스트)
    timer = 0  # 타이머
    end_time = [None] * len(at)  # end_time
    gantt = [["" for j in range(sum(bt) + 10)] for j in range(pn)]  # make empty gantt 2 dimensional list
    power_used = 0

    wtime = [0] * len(at)#NEW

    tq_wait_queue = []  # time_quantum ready_q
    t_q_counter = [time_quantum] * pn  # calculate last time_quantum

    for i in range(pn):
        gantt[i][0] = gantt_default[i]  # 간트 차트 초기값 'P','E' 입력

    while True:  # 무한 반복
        used_core = 0  # 전력이 소비된 프로세서

        if timer in at:  # Arrival_Time -> Ready_Queue
            ready_queue.append(at.index(timer))

        while len(tq_wait_queue) != 0:
            ready_queue.append(tq_wait_queue.pop(0))

        for processor_n in range(pn):  # Processor(Core) -> 0부터 시작

            if processor_n in line:  # 만약 라인 리스트에 n번째 프로세서가 잡히면

                # 프로세스 추출
                process_num = line.index(processor_n)

                if gantt[processor_n][0] == 'P':  # Processor == 'P'
                    bt[process_num] -= 2  # 실행 시간 -2 (P)
                    power_used += 3  # 3W (P)
                    used_core += 1  # 전력 소비
                    t_q_counter[processor_n] -= 1

                    if t_q_counter[processor_n] == 0:  # 만약 time_qauntum 만큼 사용했다면
                        line[process_num] = 'None'  # burst 남아있다는 기준 하에 tq_wait_queue에 넣고 다음 차례 시작
                        if bt[process_num] > 0:
                            tq_wait_queue.append(process_num)
                        else:
                            end_time[process_num] = timer + 1

                    elif bt[process_num] <= 0:  # 만약 실행시간이 0이하 (P일 때 -1도 될수 있으니)
                        line[process_num] = 'None'  # 라인큐에서 제거
                        end_time[process_num] = timer + 1
                    t_q_counter[processor_n] = time_quantum  # time_qauntum 초기하


                else:  # Processor == 'E'
                    bt[process_num] -= 1  # 실행 시간 -1 (E)
                    power_used += 1  # 1W (E)
                    used_core += 1  # 전력 소비
                    t_q_counter[processor_n] -= 1

                    if t_q_counter[processor_n] == 0:
                        line[process_num] = 'None'
                        if bt[process_num] > 0:
                            ready_queue.append(process_num)
                        else:
                            end_time[process_num] = timer + 1
                        t_q_counter[processor_n] = time_quantum
                    elif bt[process_num] <= 0:  # 만약 실행시간이 0이하 (P일 때 -1도 될수 있으니)
                        line[process_num] = 'None'  # 라인큐에서 나가리
                        end_time[process_num] = timer + 1

                gantt[processor_n][timer + 1] = col_gantt.colors(process_num)  # 간트에 집어 넣음

            elif len(ready_queue) != 0:  # 레디큐가 안비워져 있으면 && line에 잡히는 것이 없다면
                process_num = ready_queue.pop(0)  # 첫번째 값을 꺼내고 삭제한다.

                if gantt[processor_n][0] == 'P':
                    bt[process_num] -= 2  # 실행 시간 -2 (P)
                    power_used += 3  # 3W (P)
                    used_core += 1  # 전력 소비

                else:
                    bt[process_num] -= 1  # 실행 시간 -1 (E)
                    power_used += 1  # 1W (E)
                    used_core += 1  # 전력 소비

                gantt[processor_n][timer + 1] = col_gantt.colors(process_num)  # 간트에 집어 넣음

                if bt[process_num] > 0:
                    line[process_num] = processor_n  # 해당 번째 processor를 다음에도 사용하겠습니다.
                    t_q_counter[processor_n] -= 1
                else:
                    end_time[process_num] = timer + 1

            else:  # 빈 것 -> 흰 것
                gantt[processor_n][timer + 1] = 'White'

            power_used += (0.1 * (pn - used_core))  # 대기 전력

        if max(bt) <= 0:
            break



        for i in ready_queue :#NEW
            wtime[i] += 1#NEW

        timer += 1

    ttime = time_calculator.turnaround_time(at, end_time)
    ntime = time_calculator.normalized_tt(ttime, bt_copy)

    return gantt, power_used, ttime, wtime, ntime