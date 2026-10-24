class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nonzero_sum = 1
        zero_count = 0

        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                nonzero_sum *= n
        
        output = []
        for n in nums:
            if zero_count >= 2:
                output.append(0)
            elif zero_count == 1:
                if n == 0:
                    output.append(nonzero_sum)
                else:
                    output.append(0)
            else:
                output.append(nonzero_sum // n)

        return output