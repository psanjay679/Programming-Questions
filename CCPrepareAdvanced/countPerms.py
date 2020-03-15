global ans
import copy
def findPerms(nums, i, res):

    global ans

    if i == len(nums):
        ans.append(copy.copy(nums))
    else:
        for s in range(i, len(nums)):
            nums[i], nums[s] = nums[s], nums[i]
            findPerms(nums, i + 1, res)
            nums[i], nums[s] = nums[s], nums[i]

def main():
    global ans, res

    nums = [1, 2, 3]
    res = list()
    ans = list()
    findPerms(nums, 0, res)
    print(ans)


if __name__ == '__main__':

    main()