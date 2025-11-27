from typing import List


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 1:
        return intervals

    intervals.sort(key=lambda x: x[0])

    output = []
    cur = intervals[0]

    for i in range(1, len(intervals)):
        added = False
        if cur[1] < intervals[i][0]:
            output += [cur]
            cur = intervals[i]
        elif cur[0] > intervals[i][1]:
            output += [intervals[i]]
            added = True
        else:
            cur[0] = min(cur[0], intervals[i][0])
            cur[1] = max(cur[1], intervals[i][1])

    if added == False:
        print("output", output)
        print("option1", output + [cur])
        return output + [cur]
    print("option2", output)
    return output
