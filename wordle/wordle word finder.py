def load_words( ):
    #this function returns a list of words in bombparty
    wordlist =[]
    print ("Loading word list from file...")
    inFile = open ('wordleWordList.txt', 'r')
    myline = inFile.readline()
    while myline:
        #print(myline[:-1]) #this :-1 is needed to remove the \n
        if len(myline[:-1]) == 5:
            wordlist.append(myline[:-1].lower()) 
        myline = inFile.readline()
    print (len(wordlist), "words loaded." )
    return wordlist

words = load_words()


def Search(wordlist,search,bannedletters):
    #this fuction searches a list of strings and returns a list of strings that contain the search key
    fittedwords = []
    print("Searching wordlist with",search,"and avoiding the letters of",bannedletters)
    for word in wordlist:
        flag=False
        for i in range(len(word)):
            if word[i] in bannedletters: flag=True
        if flag==True: continue
        #filtered the itteration to one that does not containe grayed letters
        
        flag=False
        for i in range(len(word)):
            if search[i]==".": continue
            if word[i]!=search[i]:
                flag=True
                break
        
        if flag==False:
            fittedwords.append(word)
        else:
            pass
            #print(word,"had letters to use, but the letters did not fit in the search")
    print("Search done")


    return fittedwords


def take_inputs():
    word = input("\nenter known letter places, '.' for an unknown: ")
    notletters= input("type all the letters not availible: ")
    return word,notletters



"""
What we have done so far is make a list using the green and black letter rule, but now we will
itterate though that list to produce a list using the yellow letter rule
"""

def listCutDown(wordList):
    listoletters = input("\nenter letters that you know exist somewhere else: ")
    newwords=[]
    for word in wordList:
        Flag=0
        for letter in listoletters:
            if letter in word: Flag+=1
        if Flag==len(listoletters):
            newwords.append(word)
    return newwords

while True:
    wordsearch, notletters = take_inputs()
    correctWordList = Search(words, wordsearch, notletters)
    #print(correctWordList)
    refinedWordList = listCutDown(correctWordList)
    if len(refinedWordList) == 1:
        #special case for when theres only one option
        print("CONGRATULATIONS !!!! THE WORD YOURE LOOKING FOR IS.........")
        from time import sleep
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(2)
        print(refinedWordList[0]+"!!!!!!!!!!!!!!!111")
    else:
        print("refined list is: ",refinedWordList)
    #for letter in "Hello World":
    #    if letter not in "elor":
    #        print(letter)
