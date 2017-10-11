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

    i = 0

    while(len(l) or len(ready)):
        while(len(l) and l[0][0] <= time):
            ready.append(l[0])
            l.pop(0)
        
        if(len(ready)):
            p = ready[0]
            ready.pop(0)

            wait += time - p[0]

            if(answd[i] != True):
                firstcome[i] = p[0]
                ans += time - p[0]
                answd[i] = True

            if(p[1] <= quantum):
                time += p[1]
                p[1] = 0
            else:
                time += quantum
                p[1] -= quantum

            while(len(l) and l[0][0] <= time):
                ready.append(l[0])
                l.pop(0)

            if(p[1] > 0):
                p[0] = time
                ready.append(p)
            else:
                ret += time - firstcome[i]

        else:
            time = ready[0][0]
        
        i = (i+1)%len(answd)


    if(qtd > 0):
        print "RR", (ret/qtd), ((ans + 2)/qtd), (wait/qtd)