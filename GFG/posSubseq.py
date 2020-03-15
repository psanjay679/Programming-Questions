def cntPosSS(ar):


    pos = 0
    neg = 0

    for i in range(len(ar)):
        if ar[i] < 0:
            neg += 1
        elif ar[i] > 0:
            pos += 1

    if neg == 0:
        return (2 ** pos - 1) % 1000000007
    if pos == 0:
        return (2 ** (neg - 1) - 1) % 1000000007
    else:
        ps = 2 ** pos - 1
        pn = 2 ** pos * (2 ** (neg - 1) - 1)

        return (ps + pn) % 1000000007

if __name__ == '__main__':

    import sys
    t = int(input())

    for _ in range(t):
        n = int(input())
        ar = [int(k) for k in sys.stdin.readline().split()]
        print(cntPosSS(ar))

