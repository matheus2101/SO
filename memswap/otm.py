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
    oc = []
    for element in aux:
        oc.append(0)

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
                oc[i] = l.index(aux[i])
            index = oc[0]
            for i in range(len(oc)):
                if oc[i] > index and aux[i] in mem:
                    index = i
            mem[mem.index(aux[index])] = page
            l.pop(page)

    print "OTM", miss