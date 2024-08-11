class Solution(object):
    def leftRightDifference(self, nums):
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        answer = [0] * n
        
        
        current_left_sum = 0
        for i in range(n):
            leftSum[i] = current_left_sum
            current_left_sum += nums[i]

        
        current_right_sum = 0
        for i in range(n - 1, -1, -1):
            rightSum[i] = current_right_sum
            current_right_sum += nums[i]

    
        for i in range(n):
            answer[i] = abs(leftSum[i] - rightSum[i])

        return answer


solution = Solution()

nums1 = [10, 4, 8, 3]
nums2 = [1]

print(solution.leftRightDifference(nums1))  
print(solution.leftRightDifference(nums2))  
