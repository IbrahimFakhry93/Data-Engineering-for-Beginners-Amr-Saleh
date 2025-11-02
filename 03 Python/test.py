nums = list(map(int, input().split()))


def sum_list(nums):
    sum = 0
    for i in nums:
        sum += i
    print(sum)


sum_list(nums)
