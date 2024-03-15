class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        meetings = {}
        for i in intervals:
            for i in range(i[0], i[-1], 1):
                if i in meetings:
                    return False
                else:
                    meetings[i] = 1
        return True
            
        