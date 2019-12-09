
l = [0,1,0,0,1,1,0]
print('hi')
def binSort(a):
    i=0 #list iterator
    x=0 #left_zero counter
    y=0 #right_zero counter
    z=0 #total zero counter
    coc=0   #consecutive zero counter

    while i<len(a):
        while i !=0:
            continue
        if a[i]==0:
            z+=1
            x=i
            i+=1
            while a[i]=0:
                z+=1
                coc+=1
                i+=1
                continue
        while a[i]!=0:
            i+=1
            continue
        y=i
        a[x:y-coc-2] = a[x+1+coc:y-1]
        i = y-coc-2+1
        print('hi')
        print(a)
    return a

print(binSort(l))