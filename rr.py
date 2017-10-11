def rr(l, quantum):
    ret = 0.0
    ans = 0.0
    wait = 0.0
    time = 0
    qtd = len(l)
    ready = []
    answd = []
    for element in l:
        answd.append(False)
    firstcome = [0, 0, 0, 0]

    dic = dict(enumerate(l))

    while(len(l) or len(ready)):
        while(len(l) and l[0][0] <= time):
            ready.append(l[0])
            l.pop(0)
        
        if(len(ready)):
            p = ready[0]
            procid = 0
            ready.pop(0)

            for pid, proc in dic.items():
                if proc == p:
                    procid = pid

            wait += time - p[0]

            if(answd[procid] != True):
                firstcome[procid] = p[0]
                ans += time - p[0]
                answd[procid] = True

            if(p[1] <= quantum):
                time += p[1]
                p[1] = 0
            else:
                time += quantum
                p[1] -= quantum

            dic[procid] = p

            while(len(l) and l[0][0] <= time):
                ready.append(l[0])
                l.pop(0)

            if(p[1] > 0):
                p[0] = time
                ready.append(p)
            else:
                ret += time - firstcome[procid]

        else:
            time = ready[0][0]
    

    if(qtd > 0):
        print "RR", (ret/qtd), ((ans)/qtd), (wait/qtd)