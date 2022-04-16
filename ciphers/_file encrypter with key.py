print("""
╔══════════════════════════════════════╗
║ Welcome to my file encypter with key ║
╚══════════════════════════════════════╝
""")
print()

endecode = ""
ed = ("e","d")
while endecode not in ed:
    print("encode(e) or decode(d)")
    endecode = input("► ")
    print("-----------------")

if endecode == "e":
    print("enter file name to encrypt")
    fileName = input("► ")
elif endecode == "d":
    print("enter file name to decrypt")
    fileName = input("► ")
print("-----------------")
print("Enter file extension")
extension = input("► ")

print(fileName+"."+extension)
myFile = open (fileName+"."+extension, "rt")
phrase = myFile.read()
myFile.close()
phrase = str(phrase)
NewPhrase = ""

keyLetter = ""
print("Enter Key")
key = str(input("► "))
keyCurrent = -1
def defineKeyCurrent(keyCurrent, key):
    keyCurrent = int(keyCurrent) + 1
    if keyCurrent == len(key):
        keyCurrent = 0
    return keyCurrent

for number in range(len(phrase)):
    number = int(number)
    letter = phrase[number]
    number = ord(letter)
    
    keyCurrent = defineKeyCurrent(keyCurrent, key)
    letterel = key[keyCurrent]
    # FOR TESTING KEYWORD print("keyletter:", keyLetter)
    shift = ord(letterel)
    if endecode == "e":
        number = number + shift
    elif endecode == "d":
        number = number - shift
    number = number % 127
    NewLetter = chr(number)
    NewPhrase = NewPhrase + NewLetter


print("-----------------")
if endecode == "e":
    print("The encoded message is:")
elif endecode == "d":
    print("The decoded message is:")
print(NewPhrase)

if endecode == "e":
    myFile = open (fileName+" encoded"+"."+extension, "wt")
    myFile.write(NewPhrase)
    myFile.close()
elif endecode == "d":
    myFile = open (fileName+" decoded"+"."+extension, "wt")
    myFile.write(NewPhrase)
    myFile.close()
input()









