if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = [i for i in set(arr)]
    arr.remove(max(arr))
    print(max(arr))