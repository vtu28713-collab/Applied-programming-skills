class Solution:
    def finalPrices(self, prices):
        stack = []

        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                j = stack.pop()
                prices[j] -= prices[i]

            stack.append(i)

        return prices