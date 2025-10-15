from typing import List


def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    output = []

    for i in range(len(intervals)):
        if intervals[i][0] > newInterval[1]:
            print("first case")
            return output + [newInterval] + intervals[i:]
        elif intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            print("second case")
        else:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            print("third case")
        print(f"for loop {i}", output)
    return output + [newInterval]
