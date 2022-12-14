# @arg arr The input list like object to be sorted
# @arg cmp A compare function which takes two element in the array, 
#          cmp(a,b)<0   if a should be placed before b,
#          cmp(a,b)==0  if arr is still sorted after a and b are exchanged,
#          cmp(a,b)>0   if a should be placed behind b.
import numpy as np

def multi_sort(arr, cmp, method="None"):
    if(method=="quick"):
        quick_sort(arr,cmp)
    elif(method=="merge"):
        merge_sort(arr,cmp)
    elif(method=="None"): # do nothing
        return
    else:
        print("invalid argument!")




# must be in-place sort
def merge_sort(arr,cmp):
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left, cmp)
    right = merge_sort(right, cmp)

    # sort
    output = []
    while left and right:
        if cmp(left[0], right[0]) > 0:
            output.append(right.pop(0))
        else:
            output.append(left.pop(0))
    if left:
        output = output.extend(left)
    if right:
        output = output.extend(right)
# must be in-place sort
def quick_sort(arr,cmp):
    if len(arr) <= 1:
        return arr
    pvt = arr[np.random.randint(len(arr))]
    arrSmall = []
    arrMid = []
    arrLarge = []
    for e in arr :
        if (cmp(pvt,e) > 0):
            arrSmall.append(e)
        elif (cmp(pvt,e) < 0):
            arrLarge.append(e)
        else:
            arrMid.append(e)
    arrSmall = quick_sort(arrSmall,cmp)
    arrLarge = quick_sort(arrLarge,cmp)
    arr = arrSmall + arrMid + arrLarge
    return arr
    