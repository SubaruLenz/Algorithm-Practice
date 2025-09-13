def twoSum(self, nums: List[int], target: int) -> List[int]:
    preMap = {}  # Dictionary to store number and its index
    for i, n in enumerate(nums):
        diff = target - n  # Difference needed to reach the target
        if diff in preMap:  # Check if the complement (diff) is in the dictionary
            return [preMap[diff], i]  # Return indices of the two numbers
        preMap[n] = i  # Store the current number and its index in the map
    return []  # If no solution is found, return an empty list