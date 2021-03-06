 '''In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.'''
 def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        size = days[-1]
        max_cost = costs[0]*len(days)
        days = set(days)
        dp = [0]+size*[max_cost]
        
        for day in range(1,len(dp)):
            if day not in days:
                dp[day]=dp[day-1]
                continue
            if day > 30:
                dp[day] = min(dp[day-1]+costs[0], dp[day-7]+costs[1], dp[day-30]+costs[2])
            elif day > 7:
                dp[day] = min(dp[day-1]+costs[0], dp[day-7]+costs[1], dp[0]+costs[2])
            else:
                dp[day] = min(dp[day-1]+costs[0], dp[0]+costs[1])
        return dp[-1]