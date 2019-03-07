# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
# dynamic programming
# takes 2 sequences of letters and prints the length of the common subsequence

seq1 = input()
seq2 = input()

arr = [[-1] * len(seq1) for i in range(len(seq2))]  # use an array for memotization


def recursiveCheck(x, y):
    if x < 0 or y < 0:  # if out of bounds
        return 0
    elif arr[y][x] != -1:  # if seen before
        return arr[y][x]
    else:
        if seq1[x] == seq2[y]:
            arr[y][x] = 1 + recursiveCheck(x-1, y-1)
            return arr[y][x]

        else:
            arr[y][x] = max(recursiveCheck(x, y-1), recursiveCheck(x-1, y))
            return arr[y][x]


print(recursiveCheck(len(seq1)-1, len(seq2)-1))
