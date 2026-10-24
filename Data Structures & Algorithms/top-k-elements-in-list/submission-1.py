class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        
        for n in nums:
            myMap[n] = 1 + myMap.get(n, 0)

        maximums = []
        while len(maximums) < k:
            cmax_value = 0
            cmax_key = None

            for n in nums:
                if myMap[n] > cmax_value:
                    cmax_value = myMap[n]
                    cmax_key = n
            maximums.append(cmax_key)
            myMap[cmax_key] = 0
        
        return maximums