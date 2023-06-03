
def prepare_strings(out):
    temp = ""
    split = str(list(str(out)))
    final_result = []
    for char in range(0, len(split)-3):
        if split[char] != "\\" and split[char + 1] != "r" or split[char] == "\\" and split[char + 1] != "r":
            temp += split[char]
        else:
            final_result.append(temp)
            temp = ""
    return final_result


def clean_path(path) -> str:
    result = ""
    for char in path:
        if char != "/":
            result += char
        else:
            result = ""
    return result
