class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        forwardProd = 1
        backwardProd = 1
        fwd = []
        back = []
        newLst = list()

        for i in range(len(nums)):
            forwardProd *= nums[i] 
            fwd.append(forwardProd)

        i = length - 1
        for i in range(len(nums)):
            back.append(1)
        while i >= 0:
            backwardProd *= nums[i]
            back[i] = (backwardProd)
            i -= 1

        newLst.append(back[1])
        for i in range (1, length - 1):
            newLst.append(fwd[i - 1] * back[i + 1])

        newLst.append(fwd[length - 2])

        return newLst