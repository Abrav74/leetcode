from typing import List


def threeSum(self, nums: List[int]) -> List[List[int]]:

    output = []
    nums.sort()

    for i, part_1 in enumerate(nums):
        if i > 0 and part_1 == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums) - 1
        while l < r:
            total = part_1 + nums[l] + nums[r]

            if total > 0:
                r -= 1
            elif total < 0:
                l += 1
            else:
                output.append([part_1, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    return output
