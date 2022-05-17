class Solution:
    #  3, 2,  4, 5
    # 40, 20, 5, 1
    #  1, 3,  6, 24
    #         , 24
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = []
        post = 1
        pre = 1

        for i in range(size):
            res.append(pre)
            pre *= nums[i]

        for i in range(size - 1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res
                