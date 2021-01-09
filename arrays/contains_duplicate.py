# 1-liner - O(n) space, O(n) time
def contains_duplicate1(nums):
        return len(nums) != len(set(nums))

# O(n) space, O(n) time
def contains_duplicate2(nums):
        num_set = set()
        
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False
        
# O(1) space, O(nlogn) time
def contains_duplicate3(nums):
        nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
