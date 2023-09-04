# 先依照區間起點排序(可排除前個區間落在下個區間後面的狀況)，再根據是否重疊合併區間
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            last = merged[-1]

            if curr[0] <= last[1]:
                merged[-1] = [last[0], max(last[1], curr[1])]  # 重疊時，終點取區間最大值
            else:
                merged.append(curr)  # 不重疊時
        
        return merged
