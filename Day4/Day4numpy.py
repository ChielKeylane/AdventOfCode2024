import numpy as np

file = open("example.txt")

O = ['O']*16
words = np.vstack((O,O,O))

while True:
    content=file.readline()
    if not content:
        break
    content = list(content)
    content = [x for x in content if x != '\n']
    content.append('O')
    content.append('O')
    content.append('O')
    content.insert(0, 'O')
    content.insert(0, 'O')
    content.insert(0, 'O')
    words = np.vstack((words, content))
words = np.vstack((words,O,O,O))

allresults = []
for y in range(words.shape[0]):
    for x in range(words.shape[0]):
        letter = words[y][x]
        if letter == 'X':
            result1 = letter + words[y][x+1] + words[y][x+2] + words[y][x+3]
            allresults.append(result1)

            result2 = letter + words[y][x-1] + words[y][x-2] + words[y][x-3]
            allresults.append(result2)

            result3 = letter + words[y+1][x] + words[y+2][x] + words[y+3][x]
            allresults.append(result3)

            result4 = letter + words[y-1][x] + words[y-3][x] + words[y-3][x]
            allresults.append(result4)

            result5 = letter + words[y+1][x+1] + words[y+2][x+2] + words[y+3][x+3]
            allresults.append(result5)

            result6 = letter + words[y-1][x+1] + words[y-2][x+2] + words[y-3][x+3]
            allresults.append(result6)

            result7 = letter + words[y-1][x-1] + words[y-2][x-2] + words[y-3][x-3]
            allresults.append(result7)

            result8 = letter + words[y+1][x-1] + words[y+2][x-2] + words[y+3][x-3]
            allresults.append(result8)

counter = 0
for c in allresults:
    if c == 'XMAS':
        counter = counter+1

print(allresults)
print(counter)


