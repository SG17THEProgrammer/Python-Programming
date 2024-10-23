class Problem_724:
    def pivotIndex(self, nums):
        total = sum(nums)

        leftSum = 0
        for i in range(len(nums)):
            if leftSum == total - leftSum - nums[i]:  # leftSum == rightSum
                return i
            leftSum += nums[i]
                
            return -1
        