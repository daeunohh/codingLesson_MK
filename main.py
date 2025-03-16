import sys
sys.stdin = open("sample_input.txt", "r")

import queue
T = int(input())
for test_case in range(1, T + 1):
    mmap = []
    N = int(input())
    wormholes = dict()
    for i in range(6,11):
        wormholes[i] = list()
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(N):
            if 6 <= line[j] and line[j] <= 10:
                wormholes[line[j]].append([i,j])
        mmap.append(list)

    nextDir = [[], [1, 3, 0, 2], [3, 0, 1, 2], [2, 0, 3, 1], [1, 2, 3, 0], [1, 0, 3, 2]]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for starti in range(N):
        for startj in range(N):
            if mmap[starti][startj] != 0:
                continue
            maxScore = 0
            q = queue.Queue()
            for dir in range(4):
                q.put(starti, startj, dir, 0)        # i j dir score

            while not q.empty():
                i, j, dir, score = q.get()
                if i < 0 or j >= N: # out of map
                    score += 1
                elif 1 <= mmap[i][j] and mmap[i][j] <= 5:   # block
                    score += 1
                    dir = nextDir[dir]
                elif mmap[i][j] == -1:  # Black Holes
                    maxScore = max(maxScore, score)
                    break
                elif 6 <= mmap[i][j] and mmap[i][j] <= 10:
                    break

                while True:
                    nexti = i + dx[dir]
                    nextj = j + dy[dir]
                    if mmap[nexti][nextj] == 0:
                        continue
                    else:
                        q.put((nexti, nextj, dir, score))


    print(mmap)
    break

    # ///////////////////////////////////////////////////////////////////////////////////
