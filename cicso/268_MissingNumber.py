nums = [9,6,4,2,3,5,7,0,1]
n = len(nums)
total = n*(n+1)/2
for i in nums:
    total = total - i
print(total)