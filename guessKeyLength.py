import functools
import operator
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

# plot the graph
def plot(x, y, c, gram):
    plt.scatter(y, x, marker='o', edgecolors=c)
    plt.xlabel("Key-Lengths Suggestion")
    plt.ylabel(str(gram)+"-Grams")
    plt.show()


# guess the probable key-length from the factors' list of the corresponding distance of the n-grams
def probableKeyLength(lst):
    keyLength= dict()
    for num in lst:
        keyLength[num] = sum(map(lambda x: 1 if num == x else 0, lst))
    maxm = max(keyLength.items(), key=operator.itemgetter(1))[0]
    if maxm == 1:
        del keyLength[maxm]
        return max(keyLength.items(), key=operator.itemgetter(1))[0]
    return maxm

# re-formats the n-grams distances' factors for plotting
def getFlattenedPlotData(grams_factors_distance_map):
    x = list()
    y = list()
    for k, v in grams_factors_distance_map.items():
        x += [k for i in v]
        y += [i for i in v]
    return x, y


# reduces the factors within (mod 26)
def getFactorsInMod26(num):
    factors = list()
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(abs(i % 26))
    return factors


# calculates the distances between the n-grams
def find_factors_distances(ngrams):
    distances = dict()
    for k, v in ngrams.items():
        lst = list(map(lambda x: getFactorsInMod26(x), v[1]))
        distances[k] = set(functools.reduce(lambda a, b: a + b, lst))
    return distances


# creates n-grams from cipher text
def ngram(n, cipher):
    grams = [cipher[idx: idx + n] for idx in range(len(cipher) - 1)]
    res = Counter(grams)
    res = {k: v for k, v in res.items() if v > 1}
    ngram_map = dict()
    for k, v in res.items():
        indices = [i for i, x in enumerate(grams) if x == k]
        distance = np.diff(indices)
        ngram_map[k] = (v, list(distance))
    return ngram_map


# Analyze the cipher text for guessing the probable key length
def analyze(cipher):

    ## 3-gram analysis
    print("3-gram analysis")
    tri_grams = ngram(3, cipher)
    print("Tri-grams (occurrences, distances between them)", tri_grams)
    tri_grams_factors_distance_map = find_factors_distances(tri_grams)
    x, y = getFlattenedPlotData(tri_grams_factors_distance_map)
    print("Analysis of the difference between the distances of the 3-grams.")
    print("3-grams factors analysis plot(blue dots).")
    plot(x, y, "b", 3)
    keyLength = probableKeyLength(y)
    print("KeyLength Suggestion from 3-gram :", keyLength)

    ## 4-gram analysis
    print()
    print("4-gram analysis")
    tetra_gram = ngram(4, cipher)
    print("Tetra-grams (occurrences, distances between them)", tetra_gram)
    tetra_grams_factors_distance_map = find_factors_distances(tetra_gram)
    x, y = getFlattenedPlotData(tetra_grams_factors_distance_map)
    print("Analysis of the difference between the distances of the 4-grams.")
    print("4-grams factors analysis plot(red dots).")
    plot(x, y, "r", 4)
    keyLength = probableKeyLength(y)
    print("KeyLength Suggestion from 4-gram :", keyLength)

    return keyLength
