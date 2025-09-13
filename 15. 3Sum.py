class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        else:
            result = []
            sum = []
            nums.sort()
            seen = set()
            for i in range(len(nums)-2):
                for j in range(i+1, len(nums)-1):
                    filtered = nums[j+1:]
                    if -(nums[i] + nums[j]) in filtered:
                        sum = [nums[i], nums[j], -(nums[i]+nums[j])]
                        if tuple(sum) not in seen:
                            result.append(sum)
                            seen.add(tuple(sum))
            return result