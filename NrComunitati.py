def nrComunitati(repres):
    n=len(repres)
    aux=[0]*12
    nr=0
    for i in range(n):
        aux[repres[i]]=repres.count(repres[i])
    for x in aux:
        if x!=0:
            nr=nr+1
    return nr