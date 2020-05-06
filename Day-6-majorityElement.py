class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map_ = {}
        for x in nums:
            if x not in map_:
                map_[x]=1
            else:
                map_[x]+=1
        the_majorityElement=max(map_,key=map_.get)    
        return the_majorityElement
