import math 
class Solution:
    def findComplement(self, num: int) -> int:

        n = int(math.log2(num)) + 1
        for i in range(n):  
            num = (num ^ (1 << i))  
        return num
