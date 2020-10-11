# Calculates the Index of Coincidence of the cipher text.
def calculate_IC(cipher):
    N = len(cipher)
    letterFrequency = dict()
    for char in cipher:
        letterFrequency[char] = sum(map(lambda x: 1 if char in x else 0, cipher))
    print("Frequency of the letters: ", letterFrequency)

    total = 0
    for ele in letterFrequency.values():
        total += ele * (ele - 1)
    # Index of Coincidence
    IC = total / (N * (N - 1))
    return IC


# Returns true if the IC is in Vigenere range
# For English language 0.038 ⩽ I.C(Y ) ⩽ 0.
def is_vigenere(cipher):
    ic = calculate_IC(cipher)
    print("Index of Coincidence: " + str(ic))
    if 0.06 > ic > 0.038:
        return True
    else:
        return False
