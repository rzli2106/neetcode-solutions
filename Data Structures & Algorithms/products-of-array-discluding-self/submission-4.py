class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''nonzero_sum = 1
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
            
        return output'''
        output = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output
