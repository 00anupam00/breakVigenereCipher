**overview**


The main goal of this document is to describe the various steps involved to decipher the above text. It is assumed that only English alphabets are used, and no special characters are present. It is also assumed that the text is a polyalphabetic cipher, however, that will be proved in one of the steps mentioned below.
A tool has been implemented to decrypt the text using Kasiski analysis and all the steps necessary are coded with appropriate inline comments for verbosity. The tool is written in Python language and there are 3 scripts present altogether. Each script resembles a step required to break the encryption. Inside each script there are multiple functions which does the calculations required to achieve the desired result from the step. The tool outputs the Key used to encrypt the text and the de-ciphered plain text in the console.
The results obtained from the steps by running the tool is verified/evaluated against an online web server. Using this server, the key resulted by the tool, the decrypted text can be verified.






**Illustration**


The above cipher text was provided for decryption without knowing the key. The following steps are then performed in order to decrypt the text.

Step 0. Proof that the cipher text is a Vigenère Cipher


The first step would be to confirm if the provided text is really a Vigenère Cipher i.e. a polyalphabetic cipher. For that purpose, we need to calculate the Index of Coincidence (IC) of the text.
Index of coincidence is defined as the probability of two matching letters by randomly selecting two letters from the cipher text. It is the measure of roughness of the cipher text. 


If, in a text, 
f_a  denotes the frequency of occurrence of letter A,
f_b  denotes the frequency of occurrence of letter B,and
f_c  denotes the frequency of occurrence of letter C in a cipher text with N letters,then


 IC in the English language can be defined as,

`(IC)_en= ∑((f_a  .  (f_a-1)+ f_b  .(f_b-1)+ f_c  .  (f_c-1))/(N.(N-1))) `

In the program provided, this step is calculated by the python file verifyVigenere.py. In the English language, the typical value of IC for the English language will have the value in range:
`0.06>(IC)_en>0.038`


The python script calculates the IC of the cipher text and compares the value to this range to identify if it’s a Vigenere cipher.
The input of the script is the raw cipher text in string and is provided by the main script file.
It outputs true/false and prints the corresponding result in the console.




Step 1. Guess the Key-Length
`Now that we’ve proved that the cipher text is a Vigenere cipher, in the next step of the Kaisiski analysis method is to determine the key length. A key in this case is assumed to be an English word containing plain text English letters. It is used to determine the shift of the letters of the plain text to encode. The longer the key, the harder it is to break the encryption.


The reason, we need to determine the key length is because, if a same 3-letter is key used to encrypt all the letters, it is observed that certain trigrams of the text repeats itself. It can also be coincidence that a 3-letter word repeats itself, but the most common factor of the distances between all the trigrams would strongly suggest the key length. The longer the cipher text the more the repetitions and the more confidently we can guess the length of the key. 

The whole process of guessing the key-length is divided into numerous small steps and describe how the tool results the output:

    1. Divide the cipher text in many n-grams and calculate the distance between the occurrence of each of them. 
        It is a repeating process and can be tedious for longer texts. In this tool all possible 3-grams and 4-grams of the text are analyzed.
	2. Next, the occurrence of the n-grams and all the distances between them are calculated. A typical analysis of the 3-grams in the provided cipher results:

        `Tri-grams (occurrences,distances between them) {^' XOV^': (2,[5]),(_^')V RJ^': (4,[355,145,250])…`

        The above output says, 

        3-gram **XOV** has occurred 2 times in the text and the distance between them is 5.
        Similarly, 3-gram **VRJ** has occurred 4 times in total and 355, 145, 250 are the consecutive distances between them. Similar analysis is also carried on all 4-grams.

	3. The factors of the distances calculated would provide us an idea of the key which is repeated the most and its length.
	4. The highest most common factor of all the distances between the trigrams is 5. However, it is wise to analyze other ngrams as well and compare the results for more promising results.
    5. The probable key length suggested in the ngrams analysis is 5.
    



Step 2. Perform Frequency Analysis of the probable key-letters


  Now that we have the probable key length, the next goal would be to find the exact keyword by Frequency analysis of the letters of the key compared to that of the English letters. This means the occurrence of that letter in the key word in the cipher text is calculated. For example, the below graph depicts the frequency distribution of the English letters.
 
The following are the steps carried out:
    
    1. Divide the cipher text into 5 letter words assuming each letter has been encrypted with the key (with 5 letters)
        For Example, 
        FXOVR JXOVS HTOPK GTCNYL TGVKS OORRD DWESX EOTOX THVSS 
	2. Let us assume the first letter in the key to be A. With that assumption, the following letters in the keyword would be simply (A + d), where d is the shift in the letters.
	3. Considering the first letters in the cipher text are encrypted with A, the frequency analysis of all the first letters are carried out.
 
	4. Now we compare the above distribution with the English letter distribution. The overall distribution looks similar however it seems like the letters are shifted.
	5. Next, the key is shifted with d = 1 i.e., now we assume the first letter F in FXOVR is encrypted with letter B. After substituting the shift, we get 
                Key: AAAAA  →   BAAAA
                Cipher Text: FXOVR  → EXOVR 
            EXOVR IXOVS GTOPK FTCNYL SGVKS NORRD CWESX DOTOX SHVSS 
	6. Again, the frequency distribution graph is calculated and matched with that of the English letters. This process is carried out unless a most probable match is found. The shift is noted, and the first letter of the key is found out. After subsequent operations, the most optimum shift for the first letter of the key was found out to be 5, i.e.
        The script resulted in:
                Key: AAAAA  →    FAAAA
                Cipher Text: FXOVR  →   AXOVR 
	7. Similar steps are carried out for all the other letters of the keyword and the most probable match with the English letter’s frequency distribution is found out. A sample frequency distribution graph for the 4th letter of the keyword after decrypting all the previous letters.
 
	8. At this point, the following key and the cipher text is obtained:
                Key: AAAAA  →   FLOCA
                Cipher Text: FXOVR  → AMATR 

	9. After some iterations and comparisons, the final keyword is guessed, and the script outputs it as:
                Keyword: FLOCK
	10. The decrypted cipher text is also printed out as the program output:
    
        Decrypted Cipher:
    AMATHEMATICIANABIOLOGISTANDAPHYSICISTARESITTINGINASTREETSIDECAFEWATCHINGPEOPLEGOINGINANDCOMINGOUTOFAHOUSEONTHEOTHERSIDEOFTHESTREETFIRSTTHEYSEETWOPEOPLEGOINGINTOTHEHOUSETIMEPASSESAFTERAWHILETHEYNOTICETHREEPERSONSCOMINGOUTOFTHEHOUSETHEPHYSICISTSAYSTHEINITIALMEASUREMENTWASNTACCURATETHEBIOLOGISTSAYSTHEYHAVEREPRODUCEDTHEMATHEMATICIANSAYSIFEXACTLYONEPERSONENTERSTHEHOUSETHENITWILLBEEMPTYAGAINWHENHENRYKISSINGERLEFTHARVARDANDWENTTOWASHINGTONTOSERVEINTHENIXONADMINISTRATIONHEWASASKEDBYONEHISNEWCOLLEAGUESABOUTTHEPOLTICALINFIGHTINGINACADEMIAINWASHINGTONWEREFAMOUSFORPOLITICALINTRIGUEITSOURJOBSOMEONEASKEDBUTWEREPIKERSCOMPAREDTOTHEBACKSTABBINGANDDIRTYPOLITICSATUNIVERSITIESWHYDOYOUPEOPLEFIGHTLIKETHATKISSINGERISSAIDTOHAVERESPONDEDINHISLOWGRAVELLYVOICEITSBECAUSETHESTAKESARESOLOW
