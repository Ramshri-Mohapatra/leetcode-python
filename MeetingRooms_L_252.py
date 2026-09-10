"""
Trigger - can attend all meetings

pattern - sort then check the overlaps of the current and 
last interval and exit if overlap and give false

its O(nlogn ) due to sorting
"""

def meeting(intervals):
    intervals.sort(key=lambda x:x[0])
    last = intervals[0]

    for current in intervals[1:]:

        if current[0] <= last[1]:
            print("overlap")
            return False
        last = current
    print("No overlap")
    return True
        

intervals = [[7,10],[2,4]]
# print(meeting(intervals))




"""
Meeting Rooms II (LeetCode 253, Medium)


Trigger - no of rooms required for meeting or finding simultanous meetings

Pattern - sort starts and ends and the check for roomoccupancy


"""

def meetingRooms(intervals):
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)
    rooms = 0
    max_rooms = 0

    s = e = 0

    while s < len(starts):
        if starts[s] < ends[e]:
            rooms +=1
            s+=1
        else:
            rooms -=1
            e+=1

        max_rooms = max(rooms, max_rooms)

    return max_rooms

print(meetingRooms([[0,30],[5,10],[9,20]]))
print(meetingRooms([[7,10],[2,4]]))