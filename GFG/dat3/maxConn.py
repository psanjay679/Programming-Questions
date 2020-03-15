import sys

global ans
global visited

def is_valid(mat, row, col):

    global visited

    n = len(mat)
    m = len(mat[0])

    return row >= 0 and col >= 0 and row < n and col < m and visited[row][col] is False and mat[row][col] == '*'

def check_maxConn(mat, row, col):

    global visited

    ans = 1
    visited[row][col] = True
    poss = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

    for pos in poss:
        if is_valid(mat, pos[0], pos[1]):
            ans += check_maxConn(mat, pos[0], pos[1])

    return ans

def checkMaxConn(mat, row, col):

    global visited

    visited = list()
    for _  in range(len(mat)):
        visited.append([False] * len(mat[0]))

    return check_maxConn(mat, row, col)
    # return ans

def find_ans(mat, row, col):

    max_val = 0

    for i in range(row):
        for j in range(col):

            if mat[i][j] == '.':
                prev_val = mat[i][j]
                mat[i][j] = '*'
                max_val = max(max_val, checkMaxConn(mat, i, j))
                mat[i][j] = prev_val

    print (max_val)

def main():

    t = int(sys.stdin.readline())

    for _ in range(t):
        n, m = [int(k) for k in sys.stdin.readline().split()]

        mat = list()
        for _ in range(n):
            mat.append(list(sys.stdin.readline().strip()))

        find_ans(mat, n, m)

if __name__ == '__main__':
    main()