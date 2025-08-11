from typing import List


def maxProfit(self, prices: List[int]) -> int:
    max_prof = 0
    low = prices[0]

    for i in range(1, len(prices)):
        if prices[i] < low:
            low = prices[i]
        else:
            prof = prices[i] - low
            max_prof = max(max_prof, prof)

    return max_prof
