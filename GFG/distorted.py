import sys

def smaller_left(ar):

    ans = [None]
    stack = list()
    stack.append(ar[0])

    for i in range(1, len(ar)):

        while not len(stack) and stack[-1] >= ar[i]:
            stack.pop()
        if len(stack):
            ans.append(stack[-1])
        else:
            ans.append(None)

        stack.append(ar[i])

    return ans

def smaller_right(ar):

    ans = [None]
    stack = list()
    stack.append(ar[-1])

    for i in range(len(ar) - 2, -1, -1):
        while len(stack) and stack[-1] >= ar[i]:
            stack.pop()
        if len(stack):
            ans.append(stack[-1])
        else:
            ans.append(None)
        stack.append(ar[i])

    return ans[::-1]

def is_distorted(ar):

    left = smaller_left(ar)
    right = smaller_right(ar)

    for i in range(len(ar)):
        if left[i] is not None and right[i] is not None and (left[i] < ar[i] > right[i]) and (left[i] < right[i]):
            return 'Yes'
    return 'No'

if __name__ == '__main__':

    t = int(input())
    for _ in range(t):
        n = int(input())
        ar = [int(k) for k in sys.stdin.readline().split()]
        print(is_distorted(ar))