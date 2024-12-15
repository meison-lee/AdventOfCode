spec = ["m", "u", "l", "(", "num", ",", "num", ")"]
ptr = 0
specLen = len(spec)
my_list = []

with open("../input.txt", "r") as file:
  for line in file:
    my_list.append(line)


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

def check_string(text):
    index = 0  # position in text
    ptr = 0    # position in spec
    total = 0
    temp = 0
    toggle = 1

    while index < len(text):
        print(f"Current position: index={index} ({text[index]}), ptr={ptr} ({spec[ptr]})")

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
for text in my_list:
    result += check_string(text)

print(f"Final result: {result}")
