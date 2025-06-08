from spell_checking_utils import *
from huffman_utils import *


def main():
    w2 = "cat"
    w1 = "car"

    wordToCorrect = "thiis"

    phraseForHuffman = "I love data structures"

    dist = levenshtein_distance(w1, w2)
    print(f"levenshtein_distance is {dist}")

    dist = hamming_distance(w1, w2)
    print(f"hamming_distance is {dist}")

    dist = indel_distance(w1, w2)
    print(f"indel_distance is {dist}")

    dist = improved_levenshtein_distance(w1, w2)
    print(f"improved_levenshtein_distance is {dist}")

    dist = improved_hamming_distance(w1, w2)
    print(f"improved_hamming_distance is {dist}")

    # correctedWord = correct_word(wordToCorrect)
    # print(f"Original word: {wordToCorrect},\nCorrected word: {correctedWord}")

    correctedWord = improved_correct_word(wordToCorrect)
    print(f"Original word: {wordToCorrect},\nCorrected word: {correctedWord}")

    codebook, encoded = huffman_coding(phraseForHuffman)
    print(f'compression ratio: {len(encoded) / (len(phraseForHuffman) * 8)}')
    print(codebook)
    print(encoded)


if __name__ == "__main__":
    main()
