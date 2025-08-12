from typing import List


def permute(self, nums: List[int]) -> List[List[int]]:
    # initialize results
    results = []
    # initialize tracking for used numbers
    used = [False] * len(nums)

    # define the backtrack function
    def find_combo(path=[]):
        # base case
        if len(path) == len(nums):
            results.append(path[:])
            return

        # loop through possibilites
        for i in range(len(nums)):
            # check if used, if so move on
            if used[i]:
                continue

            # let's make sure we don't use this one again for this track
            used[i] = True
            # let's add it to the path
            path.append(nums[i])

            # run through the remaining combos
            find_combo(path)

            # backtrack the path options for the next loop
            path.pop()
            used[i] = False

    find_combo([])

    return results
