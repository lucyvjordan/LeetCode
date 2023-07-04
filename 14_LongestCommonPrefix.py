# Prompt: Write a function to find the longest common prefix string amongst an array of strings.

def FindPrefix(stringlist):
    prefix = ""

    if len(stringlist[0]) < len(stringlist[1]):
        shortest = 0
        longest = 1
    else:
        shortest = 1
        longest = 0
    # finds the shortest of the first two words so no error is raised when iterating through the word

    for j in range(len(stringlist[shortest])):
        # goes through each character
        if stringlist[shortest][j] == stringlist[longest][j]:
            prefix += str(stringlist[shortest][j])
            # if characters match, add it to the prefix
        else:
            break
            # if characters do not match, quit loop, otherwise characters may be added incorrectly later, if, for example, the 20th character matches

    for i in range(len(stringlist)):
        # going through each word in the list
        if prefix in stringlist[i][:len(prefix)]:
            # if the prefix is at the start of the word, ignore
            pass
        else:
            for j in range(len(prefix)):
                # goes through as many times as the length of the prefix
                if prefix[:len(prefix)-j] in stringlist[i][:len(prefix)]:
                    # removes values from the end of the prefix and checks it against the word to see if any section of the prefix is found at the start of the word
                    # it only checks as far through the word as the length of the current prefix so that any instances where the prefix is found in the middle of the word are not counted
                    prefix = prefix[:len(prefix)-j]
                    break

    print(prefix)

stringlist = []

stringlist = ["flower", "flow", "flight"]
FindPrefix(stringlist)