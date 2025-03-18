import copy
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    num = int(input()) 
    nums_min = list()
    sortedNums_min = list()
    sortedNums_max = list()

    while num > 0 :
        digit = num % 10
        nums_min.append(digit)
        num = int(num / 10)
    N = len(nums_min)
    nums_min.reverse()
    nums_max = list(copy.deepcopy(nums_min))
    # print(nums_min, nums_max)
    
    for i in range(N):
        sortedNums_min.append([nums_min[i], -i])
        sortedNums_max.append([nums_min[i], i])
    sortedNums_min = sorted(sortedNums_min)
    sortedNums_max = sorted(sortedNums_max, reverse=True)
    # print(sortedNums_min,'\n', sortedNums_max)
    # Get nums_min
    changed = False
    for i in range(N):
        for j in range(N):
            sv = sortedNums_min[j][0]
            si = -sortedNums_min[j][1]
            if i == 0 and sv == 0:
                continue
            if nums_min[i] <= sv :
                break
            if nums_min[i] > sv and i <= si:
                tmp = nums_min[i]
                nums_min[i] = sv
                nums_min[si] = tmp
                changed = True
                break
        if changed:
            break
    # print(nums_min)
    # Get nums_max
    changed = False
    for i in range(N):
        for j in range(N):
            sv = sortedNums_max[j][0]
            si = sortedNums_max[j][1]
            if i == 0 and sv == 0:
                continue
            if nums_max[i] >= sv :
                break
            if nums_max[i] < sv and i <= si:
                tmp = nums_max[i]
                nums_max[i] = sv
                nums_max[si] = tmp
                changed = True
                break
        if changed:
            break
    
    minVal = 0
    maxVal = 0
    for i, v in (enumerate(nums_min)):
        minVal += v * 10**(N - i - 1)
    for i, v in (enumerate(nums_max)):
        maxVal += v * 10**(N - i - 1)
    # print(minVal) 

    print("#" + str(test_case) + " " + str(minVal) + " " + str(maxVal))




