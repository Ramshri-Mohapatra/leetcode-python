"""
Trigger - If asked for intervals, meetings, timetable overlap

pattern - sort thr list and add the intervals together

"""


def countMerges(intervals):

    intervals.sort(key = lambda x: x[0])
    result = [intervals[0]]

    for current in intervals[1:]:
        last = result[-1]
        if current[0] <= last[1]:
            last[1] = max(current[1], last[1])
        else:
            result.append(current)

    return result

intervals = [[1,4],[1,7]]

print(countMerges(intervals))