def dquit():
    quit()
print("""
╔═════════════════════════════╗
║ Welcome to my caeser cipher ║
╚═════════════════════════════╝
""")
print()
wordToDefine = ""

#reads from the file and saves it as 'phrase'
myFile = open ("encoded message.txt", "rt")
phrase = myFile.read()
myFile.close()
#formats phrase and determines amount of words in the phrase
phrase = phrase.lower()
phrase = phrase.strip()
phrase = phrase + " "
phraseWordsLength = phrase.count(" ") #counts the spaces to determine words
seperateWords = ("")
possibleShifts = []
possibleWords = []


phraseWords = phrase.split()
for  number in range(0,phraseWordsLength):
    wordToDefine = phraseWords[number] #goes through each word





    print("Word defined is:",wordToDefine) #used for debugging
    

    def checkWord(word):
        #this function checks if 'word' is in the english dictionary
        word = '"'+word+'", '
        with open("wordsOG.txt") as myfile:
            if word in myfile.read():
                return True
            else:
                return False

    def findNewWord(wordToDefine, shift):
        #this function takes a word and a shift to find out the new word
        alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
                    "p","q","r","s","t","u","v","w","x","y","z")
        newWordToDefine = ""
        for number in range(len(wordToDefine)):
                letter = wordToDefine[number]
                if letter in alphabet:
                    letter = letter.lower()
                    number = ord(letter) - 97
                    number = number - shift
                    number = number % 26
                    NewLetter = chr(number + 97)
                    newWordToDefine = newWordToDefine + NewLetter
                else:
                    newWordToDefine = newWordToDefine + letter
        return newWordToDefine



    
    shift = 1
    finalShift = 0
    x = 0
    #below you can see how it cycles through each shift from 1 to 26 and notes down possible values
    while x == 0:
        if finalShift == 26:
            x = 1
            break
    
        else:
            finalShift += 1
            wordToDefine = findNewWord(wordToDefine, shift)
        if checkWord(wordToDefine) == True:
            possibleWords.append(wordToDefine) #notes down found out word
            possibleShifts.append(finalShift) #notes down found out shift associated with word



    print("----------------------------------")



if len(possibleShifts) != 0: #sees if there are possible shifts
    for number in range(0,len(possibleShifts)):
        finalShift = possibleShifts[number]
        wordToDefine = possibleWords[number]
        wwcd = "Found word: "+ wordToDefine+" with key: "+ str(finalShift)
        wwcd ="""
╔"""+("═" * len(wwcd))+"════"+"""╗
║ """+"Found word: '"+wordToDefine+"' with key: "+str(finalShift)+""" ║
╚"""+("═" * len(wwcd))+"════"+"""╝
"""
        print(wwcd)
        DecodedPhrase = findNewWord(phrase, finalShift)
        DecodedPhrase = DecodedPhrase.strip()
        print("The decoded phrase is:",DecodedPhrase)
        myFile = open ("plaintext.txt", "wt")
        myFile.write(DecodedPhrase)
        myFile.close()
else:
    print("Could not decode phrase")
    input()
    dquit()

print()
print("++++++++++++++++++++++++++++++++++++")
print()


#final message to determine most used shift and to store it in a file
from statistics import mode
bestShift = mode(possibleShifts)
finalWord = findNewWord(phrase, bestShift).strip()
finalWord.strip()
finalMessage = "Most suitable phrase is: '"+finalWord+"' with key: '"+str(bestShift)+"'"
print(finalMessage)
myFile = open ("plaintext.txt", "wt")
myFile.write(finalWord)
myFile.close()











input()













