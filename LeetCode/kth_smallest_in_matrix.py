def lowerBound(ar, val):
    low = 0
    high = len(ar) - 1
    mid = -1

    while low <= high:
        mid = (low + high) // 2

        if ar[mid] <= val:
            low = mid + 1
        else:
            high = low - 1

    return mid

def countSmaller(matrix, row, col):
    cnt = 0

    for i in range(row):
        cnt += lowerBound(matrix[i], matrix[row][col])

    return cnt


class Solution:

    def kthSmallest(self, matrix, k: int) -> int:

        low = 0
        high = len(matrix) - 1
        mid = 0

        while low < high:
            mid = (low + high) // 2

            smallerNums = countSmaller(matrix, mid, 0)

            if smallerNums > k - 1:
                high = mid - 1
            elif smallerNums < k - 1:
                low = mid + 1
            else:
                return matrix[mid][0]

        row = low
        low = 0
        high = len(matrix[0]) - 1
        mid = 0

        while low <= high:
            mid = (low + high) // 2

            smallerNums = mid + countSmaller(matrix, row, mid)

            if smallerNums == k - 1:
                return matrix[row][mid]
            if smallerNums < k - 1:
                low = mid + 1
            else:
                high = mid - 1

        return matrix[row][mid]

matrix = [[1,2],[1,3]]
k = 3

s = Solution()
print(s.kthSmallest(matrix, k))