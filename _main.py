import sys
sys.stdin = open("input.txt", "r")

import copy

T = int(input())
for test_case in range(1, T + 1):
    minVal = -1
    maxVal = -1
    nums = list(map(int, input()))
    N = len(nums)

    sortedNums_min = list()
    sortedNums_max = list()    
    for i in range(N):
        sortedNums_min.append([nums[i], -i])
        sortedNums_max.append([nums[i], i])
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
            if nums[i] <= sv :
                break
            if nums[i] > sv and i <= si:
                nums[i], nums[si] = nums[si], nums[i]
                minVal = ''.join(map(str,nums))
                nums[i], nums[si] = nums[si], nums[i]
                changed = True
                break
        if changed:
            break
    if not changed:
        minVal = ''.join(map(str,nums))
    # print(nums_min)
        
    # Get nums_max
    changed = False
    for i in range(N):
        for j in range(N):
            sv = sortedNums_max[j][0]
            si = sortedNums_max[j][1]
            if i == 0 and sv == 0:
                continue
            if nums[i] >= sv :
                break
            if nums[i] < sv and i <= si:
                nums[i], nums[si] = nums[si], nums[i]
                maxVal = ''.join(map(str,nums))
                changed = True
                break
        if changed:
            break
    if not changed:
        maxVal = ''.join(map(str,nums))
    
    print("#" + str(test_case) + " " + str(minVal) + " " + str(maxVal))




