s = input("Enter a string for analysis: ")

# vovels, cosonents, lowers, uppers
count = [0, 0, 0, 0]

for ch in s:
    if(ch in "aieouAIEOU"):
        count[0] += 1
    elif('a' <= ch <= "z" or 'A' <= ch <= "Z"):
        count[1] += 1

    if('a' <= ch <= "z"):
        count[2] += 1
    elif('A' <= ch <= "Z"):
        count[3] += 1

print("Number of vovels, cosonents, lowers, uppers respectively in given string are:", count)