import sys

def isCircular(S):

    init = [0, 0]
    last_pos = [0, 1]
    cur_pos = [0, 0]
    for c in S:
        if c == 'G':
            cur_pos = [cur_pos[0] + last_pos[0], cur_pos[1] + last_pos[1]]
        elif c == 'L':
            last_pos =
        else:
            pass
        if cur_pos == init:
            return "Circular"

    return 'NOT Circular'

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        s = sys.stdin.readline().strip()