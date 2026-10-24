class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def to_day_of_year(date: str) -> int:
            month, day = map(int, date.split('-'))
            return sum(days_in_months[:month - 1]) + day
        
        start = max(to_day_of_year(arriveAlice), to_day_of_year(arriveBob))
        end = min(to_day_of_year(leaveAlice), to_day_of_year(leaveBob))
        
        return max(0, end - start + 1)