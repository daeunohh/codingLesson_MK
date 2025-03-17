# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    num = int(input()) 
    nums = list()
    minIdx = maxIdx = -1
    minVal = 9
    maxVal = 0
    i = 0
    while num > 0 :
        digit = num % 10
        nums.append(digit)
        num = int(num / 10)
        if digit < minVal :
            minIdx = i
            minVal = digit
        if digit > maxVal:
            maxIdx = i
            maxVal = digit
        i += 1
    # print(nums)
    # print(minVal, maxVal)

    # make minNum
    tmp = nums[-1]
    nums[-1] = nums[minIdx]
    nums[minIdx] = tmp
    # print(nums)

    minNum = 0
    for i in range(len(nums)):
        minNum += nums[i] * (10**i)
    # print(minNum)
    
    # Rollback
    tmp = nums[-1]
    nums[-1] = nums[minIdx]
    nums[minIdx] = tmp
    # print(nums)

    # make maxNum
    tmp = nums[-1]
    nums[-1] = nums[maxIdx]
    nums[maxIdx] = tmp
    # print(nums)

    maxNum = 0
    for i in range(len(nums)):
        maxNum += nums[i] * (10**i)
    # print(maxNum)

    print("#" + str(test_case) + " " + str(minNum) + " " + str(maxNum))

    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
