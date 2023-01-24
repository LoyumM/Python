if __name__ == '__main__':
    N = int(input())
    
array=[]

for _ in range(N):
    command=input().strip().split()
    if command[0] == 'insert' and len(command)==3:
        array.insert(int(command[1]),int(command[2]))
    elif command[0] == 'print' and len(command) == 1:
        print(array)
    elif command[0] == 'remove' and len(command) == 2:
        array.remove(int(command[1]))
    elif command[0] == 'append' and len(command) == 2:
        array.append(int(command[1]))
    elif command[0] == 'sort' and len(command) == 1:
        array.sort()
    elif command[0] == 'pop' and len(command) ==1 :
        array.pop()
    elif command[0] == 'reverse' and len(command) ==1 :
        array.reverse()
    else:
        print('Wrong command enterted')