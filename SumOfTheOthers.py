# problem on kattis
# https://open.kattis.com/problems/sumoftheothers
# simulation

while(True):
    try:
        nums = [int(i) for i in input().split()]
        for i in range(len(nums)):
            check = nums[i]
            sums = sum(nums[0:i]) + sum(nums[i+1:])
            if check == sums:
                print(check)
                break
    except EOFError:
        break
