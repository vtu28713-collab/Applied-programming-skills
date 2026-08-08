class Solution:
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)
        total = sum(nums)

        result = []
        left_sum = 0

        for i in range(n):
            x = nums[i]

            # Difference with elements on the left
            left = x * i - left_sum

            # Difference with elements on the right
            right = (total - left_sum - x) - x * (n - i - 1)

            result.append(left + right)

            left_sum += x

        return result