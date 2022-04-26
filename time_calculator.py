def waiting_time(tt, bt) :
    
    wt = [None] * len(bt) #out of range issue problem 
    #wt = []
    for i in range(0,len(bt)):
        wt[i] = tt[i] - bt[i] 
        if(wt[i]<0):
            wt[i] = 0 
    return wt

def turnaround_time(at, et) : 
    tt = [None] * len(at)  #out of range issue problem 
    #tt = []
    for i in range(0,len(at)):
        tt[i] = et[i] - at[i] 
    return tt

def normalized_tt(tt, bt) :
    ntt= [None] * len(bt)
    #ntt = [] 
    for i in range(0,len(bt)):
        if(bt[i]>0):
            ntt[i] = tt[i]/bt[i]
        else: ntt[i] = 0  
    return ntt