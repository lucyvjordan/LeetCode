"""Prompt: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:"""
# Optimised

import time
starttime = time.time()

def Convert(s, numRows):
    arrayLetters = []
    for i in range(numRows):
        arrayLetters.append([])
        # make a 2D array with the same number of arrays as rows

    currentArray = 0
    stringIndex = 0
    goingDown = True

    while stringIndex < len(s):
        # while still characters to go through
        arrayLetters[currentArray].append(s[stringIndex])
        # append the character at the current index to the current array 
        stringIndex += 1

        if currentArray == numRows - 1:
            # if at the final array
            goingDown = False
            # set going down to false as now going up back through the arrays
        elif currentArray == 0:
            # if at the first array
            goingDown = True
            # set going down to true as now going down through the arrays

        if goingDown:
            # whether going up or down through the arrays
            currentArray += 1
        else:
            currentArray -= 1
        
    zigzagString = ""
    for array in arrayLetters:
        # going through each array
        for letter in array:
            zigzagString += letter
            # appending each letter in the array to the output string
    print(zigzagString)

s = "wygdfmhddcdufweqqwceezogpmlrkwygiwjshkncxyztbkroyaskrexyaufgodbodbwbailxtcazroeblebbrfrxahstiuxjcwabbfbgsgzpsxkegdfcpoavtauxnhpaseuaftddocvkskupshkezpboiwhextqgkdmgiexpqyfkhpgehzsxpcpnoxvxdrkfydttrzghluikaqopjrnfcjjaknnpouooghiegddontzicaoaxcwjiyfnpnssrypljschsxktypvtruehzyxxztcoswschfpwrbhbnueuymxhmraqwjhxaauoifbnxtddtinkpudtyuzsqkoxeykkuortxddkjvortaahchyhpyfiprmdmdsowaoybibunizjwfarbsxbqrmnwsbipegpcmhvyhfovnuxjgvxdogmmgdudxjbendaxmpyraxuoudgtgqeeyfjltwvhutctbpngprgdulqxtpeeqvnsowizmmrwtcdoghpacbttiyjnnykonxemenoqoneyzoddzzfcmbzllsvvjveufhslrcrgtpjpzkfnjavdoqphrngktveknmbjzrqagxhkjsshmevupifayzgetltjlxpgdtkxmtxkorfblmatzbjlslqptnjasfklxoeabfbujxxgmizboszdchdbxhfblhjwmicuorzygdwgldyriofpxuoajrrbdxhsnriqncaurngczogfyaklotoscfrqopfbrvmopilmyfnhjtffardzcaoyywmjlfcgfacmxlxwzgfjoyrhutqqgjfanqlzqmbdoorpzkdywljfhzkeeekcnqdkdcrzrawdmbxwrowjtxyglwgyapqymnpxywkxcbqshlumtfdssrnuknayfcqdgfploujarnsreqgppsmrvumfxmpctwhdglxesmqmdghvtlqjvjsxsjxkbkdrnuqdontrqbidspgjpffmhxwynvumdhlxkvutmwytflelemvrdzl"
numRows = 150

Convert(s, numRows)
print(time.time() - starttime)