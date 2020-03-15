import sys


def find_min_count(s):

    start = 0
    end = start + 1

    z_one_cnt = 0
    o_zero_cnt = 0

    # 0101
    while end < len(s):
        while start < len(s) and s[start] == '1':
            start += 1

        end = start + 1

        while end < len(s) and s[end] == '0':
            end += 1

        if end < len(s):
            z_one_cnt += 1

        start = end

    # 1010
    start = 0
    while end < len(s):
        while start < len(s) and s[start] == '0':
            start += 1

        end = start + 1

        while end < len(s) and s[end] == '1':
            end += 1

        if end < len(s):
            o_zero_cnt += 1

        start = end

    return max(0, max(z_one_cnt, o_zero_cnt) - 1)


def main():

    t = int(input())

    while t > 0:
        t -= 1
        s = sys.stdin.readline().strip()

        print(find_min_count(s))


def custom_test():
    s = "0110"
    print(find_min_count(s))


if __name__ == '__main__':
    main()
    # custom_test()