def main():
    t = int(input())

    for test_case in range(1, t + 1):
        n = int(input())
        x = [int(k) for k in input().strip().split()]
        y = [int(k) for k in input().strip().split()]
        
        x.sort()
        y.sort(reverse=True)
        product = sum([a * b for a, b in zip(x, y)])
        print("Case #%d: %d" % (test_case, product))


if __name__ == "__main__":
    main()