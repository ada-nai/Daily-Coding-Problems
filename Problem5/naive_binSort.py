
l = [0,1,1,0,0,1,0]
def binSort(arr):
    for i in range(arr):
        if arr[i]  ==0:
            arr.pop(i)
            arr.append(0)
    return arr

print(binSort(l))