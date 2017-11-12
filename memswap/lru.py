def lru(l):
    mem = []
    for i in range(l[0]):
        mem.append(0)
    l.pop(0)
    miss = 0
    count = []
    for item in mem:
        count.append(0)
    clock = 0

    for page in l:
        clock += 1
        if page in mem:
            count[mem.index(page)] = clock
            continue
        else:
            miss += 1
            if 0 in mem:
                mem[mem.index(0)] = page
                count[mem.index(page)] = clock
                continue
            aux = 0
            for i in range(len(count)):
                if count[i] < count[aux]:
                    aux = i
            mem[aux] = page
            count[mem.index(page)] = clock

    print "LRU", miss