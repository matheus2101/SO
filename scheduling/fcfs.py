def fcfs(l):
    ret = 0.0
    ans = 0.0
    wait = 0.0
    time = 0
    qtd = len(l)

    while(len(l)):
        if(l[0][0] <= time):
            p = l[0]
            l.pop(0)

            ans += time - p[0]
            wait += time - p[0]

            time += p[1]
            ret += time - p[0]

    if(qtd > 0):
        print "FCFS", (ret/qtd), (ans/qtd), (wait/qtd)