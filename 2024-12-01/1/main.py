
list1, list2 = [], []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        parts = line.split()
        print(parts)
        list1.append(parts[0])
        list2.append(parts[1])

list1.sort()
list2.sort()

totalDiff = 0

for i in range(len(list1)):
    totalDiff += abs(int(list1[i]) - int(list2[i]))

print(totalDiff)

