import sys


class Item:

    def __init__(self, val):
        self.val = val
        self.freq = 1


def compare(a: Item, b: Item) -> bool:

    if a.freq > b.freq:
        return True
    elif a.freq == b.freq:
        return a.val < b.val
    else:
        return False


class Sort:

    def __init__(self, ar):

        self.ar = list()
        temp_ar = sorted(ar)
        self.ar.append(Item(temp_ar[0]))

        idx = 1

        while idx < len(temp_ar):
            if self.ar[-1].val == temp_ar[idx]:
                self.ar[-1].freq += 1
            else:
                self.ar.append(Item(temp_ar[idx]))
            idx += 1

        self.ar.sort(key=lambda k: k.freq, reverse=True)


if __name__ == '__main__':

    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        ar = list(map(int, sys.stdin.readline().split()))
        s = Sort(ar)
        ans = list()

        for v in s.ar:
            while v.freq > 0:
                ans.append(v.val)
                v.freq -= 1
        print (' '.join([str(k) for k in ans]))