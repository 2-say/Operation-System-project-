import col_gantt
import time_calculator
import copy

def wtq(arrival_time, burst_time, core_count, time_quantum, core_type):
    # 변수 ########################################################
    ready_queue_waiting_time = [0] * len(arrival_time)
    waiting_time_quantum = time_quantum
    gantt_chart = [["" for j in range(min(arrival_time) + 1)] for j in
                   range(core_count)]  # make empty gantt_chart 2 dimensional list
    process_number_and_burst_time = []
    check = False

    # 공통
    ready_queue = []  # 레디 큐
    line = [None] * len(arrival_time)  # 라인 (어떤 core에서 진행중이었는지 기억)
    end_time = [None] * len(arrival_time)  # 각 프로세스별 end_time
    waiting_time = [0] * len(arrival_time)  # 각 프로세스별 waiting_time
    time = 0  # 시간
    power_used = 0  # 소비전력
    list_ready_queue = [[]]  # ready_queue 전체 목록
    copy_burst_time = copy.deepcopy(burst_time)  # 후에 ntt계산을 위해 필요
    ##############################################################

    # 간트차트 종류 입력 ############################################
    # 각 리스트가 P인지 E인지 첫번째 칸에 입력
    for i in range(core_count):
        gantt_chart[i][0] = core_type[i]
    ##############################################################

    # 작업이 끝날때 까지 반복 ########################################
    while True:
        used_core = 0  # 사용한 프로세서 수 count

        # ready_queue에 Process 삽입 ##########################
        # timer와 arrival_time이 일치하면 ready_queue에 Process 삽입
        if time in arrival_time:
            # ready 정렬해서 다시 받기 위해서 초기화
            ready_queue = []

            # arrival_time이 같은 프로세스들이 있을 수 있을 수 있음
            # arrival_time 중복 처리
            tmp_list = list(filter(lambda x: arrival_time[x] == time, range(len(arrival_time))))
            for i in range(len(tmp_list)):
                process_number_and_burst_time.append([tmp_list[i], burst_time[tmp_list[i]]])

            # 해당하는 ArriveTime process 저장
            process_number_and_burst_time.sort(key=lambda x: (x[1], x[0]))  # burst 적은 값으로 정렬한 후 (오름차순)
            for i in process_number_and_burst_time:
                ready_queue.append(i[0])  # ready에 정렬된 값을 넣는다.

        # 작업을 진행중이지 않은 core가 생길 때마다 max_time 확인
        if check and max(ready_queue_waiting_time) >= waiting_time_quantum and len(ready_queue) >= 1:
            max_time = max(ready_queue_waiting_time)
            max_wtime_processor_num = []

            # max_time보다 waiting_time이 큰 프로세스 우선 삽입
            for i in range(len(arrival_time)):
                if ready_queue_waiting_time[i] >= waiting_time_quantum:
                    max_wtime_processor_num.append(ready_queue_waiting_time.index(max_time))
            for i in range(len(max_wtime_processor_num)):
                ready_queue.remove(max_wtime_processor_num[i])
                ready_queue.insert(i, max_wtime_processor_num[i])
            check = False
        ######################################################

        # 코어 작업 진행 #######################################
        # 한 time 사이클마다 모든 코어에 대한 검사 진행
        for core in range(core_count):
            # gantt_chart 한칸 생성
            gantt_chart[core].append('')
            # line에 현재 core가 존재하면 현재 core에서 진행중이었던 Process가 있다는 뜻
            if core in line:
                # 프로세스 추출
                process = line.index(core)

                # 현재 코어가 P 이면
                if gantt_chart[core][0] == 'P':
                    burst_time[process] -= 2  # 실행 시간 -2 (P)
                    power_used += 3  # 3W (P)
                    used_core += 1  # 전력 소비

                    # 실행시간이 0 이하이면 line에서 제거
                    if burst_time[process] <= 0:
                        line[process] = 'None'
                        end_time[process] = time + 1
                        ready_queue_waiting_time[process] = 0
                        check = True

                # 현재 코어가 E 이면
                else:
                    burst_time[process] -= 1  # 실행 시간 -1 (E)
                    power_used += 1  # 1W (E)
                    used_core += 1  # 전력 소비

                    # 실행시간이 0 이하이면 line에서 제거
                    if burst_time[process] <= 0:
                        line[process] = 'None'
                        end_time[process] = time + 1
                        ready_queue_waiting_time[process] = 0
                        check = True

                # 간트차트에 추가
                gantt_chart[core][time + 1] = col_gantt.colors(process)  # 간트에 집어 넣음

            # line에 잡히는 것이 없을 때 ready_queue가 비워져있지 않으면 ready상태인 Process가 있다는 의미
            elif len(ready_queue) != 0:
                # 첫번째 Process를 꺼내고 ready_queue에서 삭제
                process = ready_queue.pop(0)
                # ready_queue와 같은 상태를 맞춰주기 위해 같이 삭제
                process_number_and_burst_time.remove([process, burst_time[process]])
                ready_queue_waiting_time[process] = 0

                # 현재 코어가 P 이면
                if gantt_chart[core][0] == 'P':
                    burst_time[process] -= 2  # 실행 시간 -2 (P)
                    power_used += 3  # 3W (P)
                    used_core += 1  # 전력 소비

                # 현재 코어가 E 이면
                else:
                    burst_time[process] -= 1  # 실행 시간 -1 (E)
                    power_used += 1  # 1W (E)
                    used_core += 1  # 전력 소비

                # 실행시간이 남아있으면 line에 추가
                if burst_time[process] > 0:
                    line[process] = core

                # 실행시간이 남아있지 않으면 line에 추가하지 않음
                else:
                    end_time[process] = time + 1

                # 간트차트에 추가
                gantt_chart[core][time + 1] = col_gantt.colors(process)

            # line과 ready_queue 모두 비워져있으면 현재 코어는 대기상태
            else:
                gantt_chart[core][time + 1] = 'White'

            power_used += (0.1 * (core_count - used_core))  # 대기 전력

        ######################################################

        # ready_queue 출력을 위한 데이터 저장
        # 각 초당 ready_queue를 list에 추가
        list_ready_queue.append(copy.deepcopy(ready_queue))

        # 모든 Process의 burst_time이 0이하이면 종료
        if max(burst_time) <= 0:
            break

        # ready_queue에 있다는 의미는 대기중이란 뜻
        # ready_queue에 있는 모든 Process의 waiting_time 증가
        for i in ready_queue:
            waiting_time[i] += 1
            ready_queue_waiting_time[i] += 1

        # time 증가
        time += 1
    ##############################################################

    # 함수를 통해 turnaround, normalized turnaround time 계산
    turnaround_time = time_calculator.turnaround_time(arrival_time, end_time)
    normalized_turnaround_time = time_calculator.normalized_tt(turnaround_time, copy_burst_time)

    # 간트차트 공백 제거
    for i in range(len(gantt_chart)):
        for j in range(len(gantt_chart[i])):
            gantt_chart[i] = ' '.join(gantt_chart[i]).split()

    return gantt_chart, power_used, turnaround_time, waiting_time, normalized_turnaround_time, list_ready_queue
