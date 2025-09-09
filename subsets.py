from typing import List


def subsets(self, nums: List[int]) -> List[List[int]]:
    output = []

    def subset(start=0, combo=[]):
        output.append(combo[:])

        for i in range(start, len(nums)):
            combo.append(nums[i])
            subset(i + 1, combo)
            combo.pop()

    subset()
    return output
