def fifo(l):
    mem = []
    for i in range(l[0]):
        mem.append(0)
    l.pop(0)
    miss = 0
    first = 0

    for page in l:
        if page in mem:
            continue
        else:
            miss += 1
            mem[first] = page
            first = (first + 1)%len(mem)

    print "FIFO", miss