def average(array):
    s = set(array)
    result = sum(s) / len(s)
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)