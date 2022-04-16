wordToDefine = ""

print("Enter Phrase")
phrase = input()
phrase = phrase.lower()
phrase = phrase.strip()
phrase = phrase + " "
phraseWordsLength = phrase.count(" ")
print(phrase)
print(phraseWordsLength)
seperateWords = ("")



phraseWords = phrase.split()
for  number in range(0,phraseWordsLength):
    print(phraseWords[number])
    









