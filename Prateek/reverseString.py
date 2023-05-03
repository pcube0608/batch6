

def reverse_String(str):
    str1 = ""
    for i in str:
        str1 = i + str1

    return str1

str = "Pcube"
output = reverse_String(str)
print(output)
