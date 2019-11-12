def main():
    t = int(input())

    for testcase in range(1, t + 1):
        n = int(input())
        x = [int(k) for k in raw_input().strip().split()]
        y = [int(k) for k in raw_input().strip().split()]
        
        x.sort()
        y.sort(reverse=True)
        product = sum([a * b for a, b in zip(x, y)])
        print("Case #%d: %d" % (testcase, product))


if __name__ == "__main__":
    main()