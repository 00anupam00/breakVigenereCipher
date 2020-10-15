import matplotlib.pyplot as plt


# rounds off all numbers to 3 decimal points
def round_to_3(n):
    return round(n, 3)


# plot frequency analysis graph
def plot_freq_analysis(xValue, freqList, ylabel):
    plt.xlabel("Eng Letters")
    plt.ylabel(ylabel)
    plt.bar(xValue, freqList, color="red")
    plt.ylim(0, 0.10)
    plt.show()
    plt.savefig('graphs/'+ylabel+'.png')


# performs shift-analysis and transforms the cipher text according the probable key-letter
def shift_analysis(cipher, shiftBy, idx, keyLength):
    eng = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    itr = []
    itr.extend([(i * keyLength) + idx for i in range(len(cipher))])

    lst = list(cipher)
    for i, x in enumerate(cipher):
        if i in itr:
            lst[i] = eng[abs((eng.index(cipher[i]) - shiftBy) % 26)]

    transCipher = "".join(lst)
    analysis = freq_analysis_of_key_letters(transCipher)
    return analysis, transCipher


# calculates the frequency and normalizes to compare with the English letters frequency distribution graph
def freq_analysis_of_key_letters(cipher):
    str = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return [cipher.count(i) / 1000 for i in str]


# performs frequency analysis and necessary shifts of the key-letters to decrypt the cipher text.
def decrypt(cipher, keyLength):
    # Freq Analysis of English Letter
    # https://web.archive.org/web/20040603075055/http://www.data-compression.com/english.html
    freq = "0.0651738 0.0124248 0.0217339 0.0349835 0.1041442 0.0197881 0.0158610 0.0492888 0.0558094 0.0009033 0.0050529 0.0331490 0.0202124 0.0564513 0.0596302 0.0137645 0.0008606 0.0497563 0.0515760 0.0729357 0.0225134 0.0082903 0.0171272 0.0013692 0.0145984 0.0007836"
    freqList = list(map(lambda x: round_to_3(float(x)), freq.split(" ")))
    eng = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    plot_freq_analysis(eng, freqList, "Frequency of English letters")

    # Raw freq Analysis of the Key-letters
    freqAnalysis = freq_analysis_of_key_letters(cipher)
    plot_freq_analysis(eng, freqAnalysis, "No-Shift(assuming all letters as A in the key)")

    print("Freq Analysis of the key-letters with shift")
    print("Plot Graph: 1st letter of the key shifted by 5 (A -> F) chars")
    analysis, transCipher = shift_analysis(cipher, 5, 0, keyLength)
    xValue = list(map(lambda x: eng[abs((eng.index(x) + 5) % 26)], list(eng)))
    plot_freq_analysis(xValue, analysis, "+5 shifted analysis for 1st letter in Key")

    print("Plot Graph: 2nd letter of the key shifted by 11 (A -> L) chars")
    analysis, transCipher = shift_analysis(transCipher, 11, 1, keyLength)
    xValue = list(map(lambda x: eng[abs((eng.index(x) + 11) % 26)], list(eng)))
    plot_freq_analysis(xValue, analysis, "+11 shifted analysis for 2nd letter in Key")

    print("Plot Graph: 3rd letter of the key shifted by 14 (A -> O) chars")
    analysis, transCipher = shift_analysis(transCipher, 14, 2, keyLength)
    xValue = list(map(lambda x: eng[abs((eng.index(x) + 14) % 26)], list(eng)))
    plot_freq_analysis(xValue, analysis, "+14 shifted analysis for 3rd letter in Key")

    print("Plot Graph: 4th letter of the key shifted by 2 (A -> C) chars")
    analysis, transCipher = shift_analysis(transCipher, 2, 3, keyLength)
    xValue = list(map(lambda x: eng[abs((eng.index(x) + 2) % 26)], list(eng)))
    plot_freq_analysis(xValue, analysis, "+2 shifted analysis for 4th letter in Key")

    print("Plot Graph: 5th letter of the key shifted by 10 (A -> K) chars")
    analysis, transCipher = shift_analysis(transCipher, 10, 4, keyLength)
    xValue = list(map(lambda x: eng[abs((eng.index(x) + 10) % 26)], list(eng)))
    plot_freq_analysis(xValue, analysis, "+10 shifted analysis for 5th letter in Key")

    print()
    print("Keyword: FLOCK")
    print("Decrypted Cipher: ")
    print(transCipher)
