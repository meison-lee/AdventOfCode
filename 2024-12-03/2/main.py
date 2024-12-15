spec = ["m", "u", "l", "(", "num", ",", "num", ")"]
do = ["d", "o", "(", ")"]
dont = ["d", "o", "n", "'", "t", "(", ")"]
ptr = 0
specLen = len(spec)
my_list = []

with open("../input.txt", "r") as file:
  for line in file:
    my_list.append(line)


def checkDo(text, index):
    ptr = 0
    while text[index] == do[ptr]:
        if do[ptr] == ")":
            return True, index
        index += 1
        ptr += 1

    return False, index

def checkDont(text, index):
    ptr = 0
    while text[index] == dont[ptr]:
        if dont[ptr] == ")":
            return True, index
        index += 1
        ptr += 1

    return False, index


def getNumber(text, start_index, ptr):
    # Helper function to extract number from string
    num = ""
    i = start_index
    while i < len(text) and text[i].isdigit():
        num += text[i]
        i += 1
    if num == "":
        return i, -1
    return i, int(num)

def check_string(text, spec):
    index = 0  # position in text
    ptr = 0    # position in spec
    total = 0
    temp = 0
    toggle = 1

    while index < len(text):
        # print(f"Current position: index={index} ({text[index]}), ptr={ptr} ({spec[ptr]})")
        if text[index] == "d":
            res, new_index = checkDo(text, index)
            if res:
                index = new_index + 1
                toggle = 1
                continue
            res, new_index = checkDont(text, index)
            if res:
                index = new_index + 1
                toggle = 0
                continue
        if toggle == 0:
            index += 1
            continue
        # If characters don't match, reset pattern matching
        if text[index] != spec[ptr] and spec[ptr] != "num":
            index += 1
            ptr = 0
            temp = 0
            continue

        # If we reach closing parenthesis
        if spec[ptr] == ")" :
            total += temp
            ptr = 0
            index += 1
            temp = 0
            continue

        # If we're looking for a number
        if spec[ptr] == "num":
            new_index, number = getNumber(text, index, ptr)
            if number == -1:
                # No valid number found
                ptr = 0
                temp = 0
            else:
                # Valid number found
                index = new_index
                ptr += 1
                if temp == 0:
                    temp = number
                else:
                    temp *= number
            continue

        # For any other character match
        index += 1
        ptr += 1

    return total

result = 0
str = ""
for text in my_list:
    str += text
result = check_string(str, spec)

print(f"Final result: {result}")
