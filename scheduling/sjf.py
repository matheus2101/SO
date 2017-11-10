def sjf(l):
    ret = 0.0
    ans = 0.0
    wait = 0.0
    time = 0
    qtd = len(l)

    priority = []
    procOrd = []

    while(len(l) or len(priority)):
        while(len(l) and l[0][0] <= time):
            priority.append(l[0])
            l.pop(0)

        for element in priority:
            procOrd.append(element)
            priority.remove(element)

        sorted(procOrd, key=lambda proc: proc[1])

        for element in procOrd:
            priority.append(element)

        procOrd = []

        if(len(priority)):
            p = priority[0]
            priority.pop(0)

            ans += time - p[0]
            wait += time - p[0]

            time += p[1]
            ret += time - p[0]

        else:
            time = priority[0][0]

    if(qtd > 0):
        print "SJF", (ret/qtd), (ans/qtd), (wait/qtd)