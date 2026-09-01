class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                greater[smaller] = num

            stack.append(num)

        # Remaining elements have no greater element
        while stack:
            greater[stack.pop()] = -1

        return [greater[num] for num in nums1]