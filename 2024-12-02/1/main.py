my_list = []

with open("../input.txt", "r") as file:
    for line in file:
        if line.strip():  # Skip empty lines
            numbers = [int(x) for x in line.strip().split()]
            my_list.append(numbers)

def checkIncreaseExcept(list, index):
  if index == 0:
    prev = list[1] - 1
  else:
    prev = list[0] - 1

  for i in range(len(list)):
    if i == index:
      continue
    curr = list[i]
    if prev >= curr:
      return False, i
    if curr - prev > 3:
      return False, i
    prev = curr

  return True, -1

def checkDecreaseExcept(list, index):
  if index == 0:
    prev = list[1] + 1
  else:
    prev = list[0] + 1

  for i in range(len(list)):
    if i == index:
      continue
    curr = list[i]
    # print(prev, curr)
    if prev <= curr:
      return False, i
    if prev - curr > 3:
      return False, i
    prev = curr
  return True, -1

my_list = [
  [48,46,47,49,51,54,56],
  [1,1,2,3,4,5],
  [1,2,3,4,5,5],
  [5,1,2,3,4,5],
  [1,4,3,2,1],
  [1,6,7,8,9],
  [1,2,3,4,3],
  [9,8,7,6,7],
  [7,10,8,10,11],
  [29,28,27,25,26,25,22,20],
  [7,10,8,10,11],
  [29,28,27,25,26,25,22,20]
]

safe = 0
for list in my_list:
  for index in range(len(list)):
    output1,_ = checkIncreaseExcept(list, index)
    output2,_ = checkDecreaseExcept(list, index)
    if output1 or output2:
      safe += 1
      break

print(safe)


