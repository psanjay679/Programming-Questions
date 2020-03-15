def find_max(ar, n):

    if n <= 0:
        return 0

    return max(
        find_max(ar, n - 1),
        ar[n - 1] + find_max(ar, n - 2)
    )


ar = [5, 5, 10, 100, 10, 5]
print (find_max(ar, len(ar)))