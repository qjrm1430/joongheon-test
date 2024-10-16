def solution(nums):
    min = len(set(nums))
    max = len(nums) / 2
    if min > max:
        return max
    else:
        return min