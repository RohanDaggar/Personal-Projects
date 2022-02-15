def load_words( ):
    #this function returns a list of words in bombparty
    wordlist =[]
    print ("Loading word list from file...")
    inFile = open ("bombParty.txt", 'r')
    myline = inFile.readline()
    while myline:
        #print(myline)
        wordlist.append(myline[:-1].lower())
        myline = inFile.readline()
    print (len(wordlist), "words loaded." )
    return wordlist

words = load_words()

def Search(wordlist,search):
    #this fuction searches a list of strings and returns a list of strings that contain the search key
    fittedwords = []
    for word in wordlist:
        #print(search,word,search in word)
        if search in word:
            #print(word)
            fittedwords.append(word)
    print("Search done")
    return fittedwords

#search = Search(words,input("Input characters to search: ").lower())

#print(sorted(search, key=len)[-20:])


#while True:
    #longest words
#    for word in sorted(Search(words,input("Input characters to search: ").lower()), key=len)[-20:]: print(word)

import random
while True:
    #random words
    randlist = Search(words,input("Input characters to search: ").lower())
    random.shuffle(randlist)
    for word in randlist[-20:]: print(word)
    print()
