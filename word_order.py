n = int(input())

counts = {}

for _ in range(n):
    word = input()
    if word in counts:
        counts[word]+=1
    else:
        counts[word] = 1

print(len(counts))
print(*counts.values(),sep=' ')