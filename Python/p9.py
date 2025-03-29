import math

def find_multiple(arr):

    if 7 in arr:
        index = arr.index(7)
        arr = arr[index+1:]

    if arr:
        print(math.prod(arr))
    else:
        print(-1)

arr = [int(input("Enter number: ")) for num in range(0, 3)]
find_multiple(arr)


        
