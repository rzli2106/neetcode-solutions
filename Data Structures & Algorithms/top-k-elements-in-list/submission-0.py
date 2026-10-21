class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        for n in nums:
            myMap[n] = 1 + myMap.get(n, 0)
        
        maximums = []
        while len(maximums) < k:
            cmax_val = 0
            cmax_key = None
            
            for n in myMap:
                if myMap[n] > cmax_val:
                    cmax_val = myMap[n]
                    cmax_key = n
                    
            maximums.append(cmax_key)
            
            myMap[cmax_key] = 0
            
        return maximums