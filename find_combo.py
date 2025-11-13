from typing import List


def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    output = []

    def find_combo(n, target, combo=[]):
        if target == 0:
            output.append(combo.copy())
            return
        if n >= len(candidates) or target < 0:
            return

        combo.append(candidates[n])

        find_combo(n, target - candidates[n], combo)
        combo.pop()
        find_combo(n + 1, target, combo)

    find_combo(n=0, target=target)

    return output
