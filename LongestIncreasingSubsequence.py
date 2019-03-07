# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
# dynamic programming
# takes 2 sequences of numbers seperated by whitespace and prints the length and longest increasing subsequence

inp = [int(x) for x in input().split()]

# create an array to hold lengths of possible sub-sequences and indices of next sub-sequence
arr = [(1, i) for i in range(len(inp))]
longest_length = 0
longest_index = 0

for i in reversed(range(len(inp))):
    length = 1
    index = i

    for j in range(i+1, len(inp)):
        if inp[i] < inp[j]:  # we have an increasing sub-sequence
            if length < arr[j][0] + 1:  # we have a longer sub-sequence
                length = arr[j][0] + 1
                index = j

    if length > longest_length:
        longest_length = length
        longest_index = i

    arr[i] = (length, index)

print('Number of elements in longest increase subsequence:', longest_length)

print('Longest increasing subsequence is:', end=' ')
while longest_index != arr[longest_index][1]:
    print(inp[longest_index], end=' ')
    longest_index = arr[longest_index][1]

print(inp[longest_index])
