import verifyVigenere, guessKeyLength, frequencyAnalysis

if __name__ == '__main__':
    cipher = "FXOVRJXOVSHTOPKGTCNYLTGVKSOORRDDWESXEOTOXTHVSSRWPKXEFGOYDWFOHLTGGFEQJSSRDGYUWSIYNYUKXFYREYRTBIY" \
             "ZECHKMZIUOTYHJOTEVGBXTRGYKEVGCYCSGDKTFUDYSSACJPHYYUPCRVJRCKXLTBVYYSSJYZDSVSRPDCCXPGCPYPFCGMTZGDMPMPYYT" \
             "QGDMCSGZJCGQXXNCOSSRCWDTQHJOMZIUOYSSRRDDWESXEGCIXEVGSSTHKKQXSCCZCSOOSEKCCSEOEMZCOVOYSSDSTWCISXEG" \
             "CIXEVGIMLJGBJAFQNZNSFDMPACDMPACDNNWCXXLMUSKPLCMYWMQXJASTCTYSPDJCGVRJSCWCJEVGXNEKKVQMSGWUEMCQFTBY" \
             "RJYVGXWJYKCXTBIOWWSHDMLFXKWOOPNBPBVDTHOURNYUVYSECUOWGSKXYSSPSCZBCNRTBKCYCOVSTYVGGFDOUUJOPAYSPVKC" \
             "SPKEYQWSCQZPGCLTFHVRJACNDNNONSSQWIRYTBISSLQCNJXWCSSHOURNYUVYSHSTOKLAQEXQCTZTWWVSHLZKXYCWIEJTHUYZ" \
             "CXQLXZAGYSPOUUJOPWDBPFGZNVSTCHZARKWPRVYYSSDKHVGVKGMWPQFYRFSWEMRYQTHKMXLHWXNGSTCNEWGCBSMFYDZIROTA" \
             "ZGPNRVVVNVSVRFEYKCXTBIOWTGUKNOHQRFGSTOXACPNJOWPRNDZQGLCOXOQWMXYNNSKDXMSEKZDSVRJDHCUJDOTOXZZQG"

    print("STEP 1: To verify if the cipher text is encrypted with vigenere cipher")
    isVigenere = verifyVigenere.is_vigenere(cipher)
    if isVigenere: print("The IC is in range 0.06 > ic > 0.038. Hence, it can be concluded that the provided cipher is a vigenere cipher. ")
    else: print("The IC is in not in range 0.06 > ic > 0.038. Hence, the provided cipher is NOT a vigenere cipher. ")

    print()
    print()
    print('''STEP 2: Analysis for finding the probable key length
        a. Perform 3- gram and 4-gram analysis of possible key lengths
        b. Plot Graph of the n-gram analysis''')
    keyLength = guessKeyLength.analyze(cipher)

    print()
    print()
    print('''STEP 3. Perform frequency comparison of the letters with that of the English alphabets
        a. Perform necessary shifts to compare the Frequency distribution of the key-letters.
        b. Decrypt the cipher text with shifts for all the key-letters combined.''')
    frequencyAnalysis.decrypt(cipher, keyLength)
    exit(-1)
