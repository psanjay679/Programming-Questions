import sys


def getMaxElMinFreq(ar):
    map = dict()

    for a in ar:
        if a not in map:
            map[a] = 0
        map[a] += 1

    maxEl = -float("inf")
    minFreq = float("inf")

    for a in ar:

        if minFreq > map[a]:
            minFreq = map[a]
            maxEl = a
        elif minFreq == map[a]:
            maxEl = max(a, maxEl)

    return maxEl


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ar = [int(k) for k in sys.stdin.readline().split()]

        print(getMaxElMinFreq(ar))


if __name__ == '__main__':
    main()
