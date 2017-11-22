def otm(l):
    mem = []
    for i in range(l[0]):
        mem.append(0)
    l.pop(0)
    miss = 0
    count = 0

    pages = set(l)
    aux = []
    for item in pages:
        aux.append(item)
    nextoc = []
    for element in aux:
        nextoc.append(0)

    for page in l:
        count += 1
        if page in mem:
            l.pop(page)
            continue
        else:
            miss += 1
            if 0 in mem:
                mem[mem.index(0)] = page
                continue
            for i in range(len(aux)):
                nextoc[i] = l.index(aux[i])
            index = nextoc[0]
            for i in range(len(nextoc)):
                if nextoc[i] > index and aux[i] in mem:
                    index = i
            mem[mem.index(aux[index])] = page
            l.pop(page)

    print "OTM", miss