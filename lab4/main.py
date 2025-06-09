from spell_checking_utils import *
from huffman_utils import *
import time


def main():
    w2 = "cat"
    w1 = "car"

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

    start = time.time()
    correct_text()
    end = time.time()
    print(f"correct_text execution time: {end - start:.6f} seconds")

    start = time.time()
    improved_correct_text()
    end = time.time()
    print(f"improved_correct_text execution time: {end - start:.6f} seconds")

    codebook, encoded = huffman_coding(phraseForHuffman)
    print(f'compression ratio: {len(encoded) / (len(phraseForHuffman) * 8)}')
    print(codebook)
    print(encoded)


if __name__ == "__main__":
    main()
