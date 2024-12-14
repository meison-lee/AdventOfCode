list1, list2 = [], []
my_dict = {}



with open("../input.txt", "r") as file:
    for line in file:
        line = line.strip()
        parts = line.split()

        list1.append(parts[0])
        list2.append(parts[1])
        my_dict[parts[1]] = my_dict.get(parts[1], 0) + 1

similarity = 0
for num in list1:
    similarity += int(num) * my_dict.get(num, 0)
print(similarity)


