class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = {}
        for i in nums:
            if i in myMap:
                return True
            myMap[i] = 1
        return False


        