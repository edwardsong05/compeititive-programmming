# problem on kattis
# https://open.kattis.com/problems/froshweek2
# greedy algorithm

n, m = [int(i) for i in input().split()]

tasks = [int(i) for i in input().split()]
intervals = [int(i) for i in input().split()]

tasks.sort(reverse=True)
intervals.sort(reverse=True)

completed = 0
task_pointer = 0  # note that the pointer is important to reduce time in this problem

for i in intervals:
    found = False

    for j in range(task_pointer, len(tasks)):
        if tasks[j] <= i:
            completed += 1
            found = True
            task_pointer = j + 1
            break

    if task_pointer == len(tasks):
        break
    elif not found:
        break

print(completed)
