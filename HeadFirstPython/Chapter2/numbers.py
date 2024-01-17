"""
Book Head First Python, chapter 2, example, page 62

@author: Tiago
@date: Jan 24
"""
nums = [1, 2, 3, 4]
nums.remove(3)
print(nums) # -> [1, 2, 4]

print(nums.pop()) # -> if index isn't given, the last item is removed
print(nums) # -> [1, 2]

print(nums.pop(0)) # -> remove the first item
print(nums) # -> [2]

nums.extend([3, 4]) # -> [2, 3, 4]
print(nums)

nums.insert(0, 1) # -> [1, 2, 3, 4]
print(nums)

nums.insert(2, "two-and-a-half") # -> [1, 2, 'two-and-a-half', 3, 4]
print(nums)

