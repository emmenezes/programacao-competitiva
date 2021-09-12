def fat (n):
    ans = []
    for i in range(n):
        ans.append(i+1)
    
    return ans

quest = fat(20)

print(quest)

nums = list(map(int, input().split()))
fatorial = fat(nums[0]) + fat(nums[0]) + fat(nums[0]) + fat(nums[3]) + fat(nums[4])

print(fatorial)