class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 0
        last = n
        
        while (first <= last):
            mid = first + (last-first)//2
            is_bad = isBadVersion(mid)
            if is_bad:
                last = mid-1
            else:
                first = mid+1
        return first
