import sys

def manipulate(s1, s2):

    a = list()
    a.append(ord(s1[0]))

    for c in s1[1:]:
        if c == '#':
            a[-1] += 1
        else:
            a.append(ord(c))
    b = list()
    b.append(ord(s2[0]))

    for c in s2[1:]:
        if c == '#':
            b[-1] += 1
        else:
            b.append(ord(c))

    for i in range(len(a)):
        if a[i] > 90:
            a[i] = a[i] % 90 + 64
    for i in range(len(b)):
        if b[i] > 90:
            b[i] = b[i] % 90 + 65

    return 'Yes' if a == b else 'No'

def main():
    t = int(input())
    for _ in range(t):
        s1 = sys.stdin.readline().strip()
        s2 = sys.stdin.readline().strip()
        print (manipulate(s1, s2))

if __name__ == '__main__':
    main()