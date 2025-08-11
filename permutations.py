from typing import List


def permute(self, nums: List[int]) -> List[List[int]]:
    output = []

    def find_combo(combo, used):
        if len(combo) == len(nums):
            output.append(combo[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            combo.append(nums[i])
            find_combo(combo, used)
            used[i] = False
            combo.pop()

    find_combo([], [False] * len(nums))

    return output
