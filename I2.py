def read_arr():
    return [int(i) for i in input().split()]

a, b = read_arr()
arr1 = read_arr()
arr2 = read_arr()

if a < b or sum(arr1) < sum(arr2):
    print(-1)
else:
    err = 0
    s = 0
    for tgt in arr2:
        while s < tgt and arr1:
            s += arr1.pop(0)
        if s < tgt:
            break
        else:
            err += s - tgt
            s = 0
    else:
        s = -1
    if s != -1:
        print(-1)
    else:
        err += sum(arr1)
        print(err)
