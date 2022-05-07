import FCFS
import RR
import SPN
import SRTN
import HRRN
import WTT

def operator(gantt_type, scheduling_type, tq, at, bt):
    processor_number = len(gantt_type)  # Processor(Core) 개수

    if scheduling_type == "FCFS":
        return FCFS.fcfs(at, bt, processor_number, gantt_type)

    elif scheduling_type == "RR":
        return RR.rr(at, bt, processor_number, tq, gantt_type)

    elif scheduling_type == "SPN":
        return SPN.spn(at, bt, processor_number, gantt_type)

    elif scheduling_type == "SRTN":
        return SRTN.srtn(at, bt, processor_number, gantt_type)

    elif scheduling_type == "HRRN":
        return HRRN.hrrn(at, bt, processor_number, gantt_type)

    elif scheduling_type == "WTT":
        return WTT.wtt(at, bt, processor_number, gantt_type)
