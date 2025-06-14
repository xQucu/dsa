KEYBOARD = [
    ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", ""],
    ["", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "\\"],
    ["", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "", ""],
    ["", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "", "", ""]
]


def find_coords(char):
    for i, row in enumerate(KEYBOARD):
        for j, key in enumerate(row):
            if key == char:
                return (i, j)
    return None


def keyboard_char_distance(c1: str, c2: str) -> float:
    if c1 == c2:
        return 0

    coord1 = find_coords(c1)
    coord2 = find_coords(c2)

    if coord1 is None or coord2 is None:
        return 1

    squaredDistance = (coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2
    if squaredDistance <= 2:
        return 0.1
    elif squaredDistance <= 4:
        return 0.6
    else:
        return 1


def createCalculationsTable(len1, len2):
    table = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    for i in range(len1 + 1):
        table[i][0] = i
    for j in range(len2 + 1):
        table[0][j] = j
    return table


def levenshtein_distance(w1: str, w2: str) -> int:
    len1 = len(w1)
    len2 = len(w2)

    table = createCalculationsTable(len1, len2)

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            cost = 0 if w1[i - 1] == w2[j - 1] else 1
            table[i][j] = min(table[i][j - 1], table[i - 1]
                              [j], table[i - 1][j - 1])+cost

    return table[len1][len2]


def hamming_distance(w1: str, w2: str):
    len1 = len(w1)
    if len1 != len(w2):
        raise ValueError("Strings must be of equal length.")
    cost = 0

    for i in range(len1):
        cost += 0 if w1[i] == w2[i] else 1

    return cost


def indel_distance(w1, w2):
    len1 = len(w1)
    len2 = len(w2)

    table = createCalculationsTable(len1, len2)

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if w1[i - 1] == w2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = min(table[i][j - 1], table[i - 1][j]) + 1

    return table[len1][len2]


def improved_levenshtein_distance(w1, w2):

    len1 = len(w1)
    len2 = len(w2)

    table = createCalculationsTable(len1, len2)

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            cost = 0 if w1[i - 1] == w2[j -
                                        1] else keyboard_char_distance(w1[i - 1], w2[j - 1])
            table[i][j] = min(table[i][j - 1], table[i - 1]
                              [j], table[i - 1][j - 1])+cost

    return table[len1][len2]


def improved_hamming_distance(w1: str, w2: str):
    len1 = len(w1)
    if len1 != len(w2):
        raise ValueError("Strings must be of equal length.")
    cost = 0

    for i in range(len1):
        cost += 0 if w1[i] == w2[i] else keyboard_char_distance(w1[i], w2[i])

    return cost


def correct_word(w):
    with open("words_alpha.txt", "r") as f:
        for line in f:
            word = line.strip()
            if word == w:
                return word
    costsL = []
    # costsH = []
    # costsI = []
    with open("words_alpha.txt", "r") as f:
        for word in f:
            word = word.strip()
            costsL.append((word, improved_levenshtein_distance(w, word)))
            # if len(word) == len(w):
            #     costsH.append((word, improved_hamming_distance(w, word)))
            # costsI.append((word, indel_distance(w, word)))

    costsL.sort(key=lambda x: x[1])
    # costsH.sort(key=lambda x: x[1])
    # costsI.sort(key=lambda x: x[1])

    # print((costsL[0], costsH[0], costsI[0]))
    return costsL[0][0]


def improved_correct_word(w, dictionary):
    with open("words_alpha.txt", "r") as f:
        for line in f:
            word = line.strip()
            if word == w:
                return word

    wLen = len(w)
    correctedWord = w
    correctedWordCost = 100000

    if (wLen in dictionary):
        for word in dictionary[wLen]:
            if word == w:
                return word
            dist = improved_hamming_distance(w, word)
            if dist <= 1 and dist < correctedWordCost:
                correctedWord = word
                correctedWordCost = dist

    if correctedWord == w:
        return correct_word(w)

    return correctedWord


def correct_text():
    with open("corrected_text.txt", "w") as correctedFile:
        with open("corrupted_text.txt", "r") as corruptedFile:
            for line in corruptedFile:
                words = line.split(" ")
                for word in words:
                    correctedWord = correct_word(word)
                    correctedFile.write(correctedWord + " ")
                correctedFile.write("\n")


def createDictionary():
    dictionary = {}
    with open("words_alpha.txt", "r") as f:
        for word in f:
            word = word.strip()
            wordLength = len(word)
            if wordLength in dictionary:
                dictionary[wordLength].append(word)
            else:
                dictionary[wordLength] = [word]
    return dictionary


def improved_correct_text():
    dictionary = createDictionary()
    with open("improved_corrected_text.txt", "w") as correctedFile:
        with open("corrupted_text.txt", "r") as corruptedFile:
            for line in corruptedFile:
                words = line.split(" ")
                for word in words:
                    correctedWord = improved_correct_word(word, dictionary)
                    correctedFile.write(correctedWord + " ")
                correctedFile.write("\n")
