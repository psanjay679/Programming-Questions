import sys

def find_power(a, b, c):
    if b == 0:
        return 1
    if a == 0:
        return 0

    res = find_power(a, b >> 1, c)

    if b % 2 == 0:
        res = (res * res) % c
    else:
        res = (res * res * a) % c

    return res

def main():
    t = int(input())
    for _ in range(t):
        a, b, c = [int(k) for k in sys.stdin.readline().split()]
        print(find_power(a, b, c))

if __name__ == '__main__':
    main()