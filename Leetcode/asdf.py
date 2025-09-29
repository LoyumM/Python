arr = [1,17,3,12,4]

counter = 0
length = []
l = 0
for i in range(len(arr)):
    while arr[i+l] > arr[i] and i+l-1 < len(arr):
        if arr[i+l] > arr[i]:
            l += 1
            print(arr[i+l], arr[i], l)
            
        

