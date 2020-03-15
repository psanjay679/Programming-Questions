import sys

def update_matrix(n, qr):

    mat = list()
    for _ in range(n):
        mat.append([0] * n)
    max_el = 0
    for k in range(len(qr)):
        for i in range(qr[k][0]):
            for j in range(qr[k][1]):
                mat[i][j] += 1
                max_el = max(max_el, mat[i][j])

    cnt = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] < max_el:
                cnt += 1

    print (cnt)


if __name__ == '__main__':
    t = int(sys.stdin.readline())

    for _ in range(t):
        n, k = [int(k) for k in sys.stdin.readline().split()]
        qr = list()
        for _ in range(k):
            qr.append(list(int(k) for k in sys.stdin.readline().split()))
        update_matrix(n, qr)