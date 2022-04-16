print("""
╔═══════════════════════════════════╗
║ Welcome to my The Vigenère Cipher ║
╚═══════════════════════════════════╝
""")
print()
endecode = ""
ed = ("e","d")


while endecode not in ed:
    print("encode(e) or decode(d)")
    endecode = input()
    print("-----------------")

if endecode == "e":
    myFile = open ("plaintext.txt", "rt")
    phrase = myFile.read()
    myFile.close()
elif endecode == "d":
    myFile = open ("encoded message.txt", "rt")
    phrase = myFile.read()
    myFile.close()
    
phrase = str(phrase)
"""
if endecode == "e":
    print("enter phrase to encode")
elif endecode == "d":
    print("enter phrase to decode")
phrase = input()

print("-----------------")
"""
NewPhrase = ""

keyLetter = ""
print("Enter Key")
key = str(input())
keyCurrent = -1
    
def defineKeyCurrent(keyCurrent, key):
    keyCurrent = int(keyCurrent) + 1
    if keyCurrent == len(key):
        keyCurrent = 0
    return keyCurrent

#below is for testing key repetitavness
"""
x = 20
while x > 0:
    keyCurrent = defineKeyCurrent(keyCurrent, key)
    keyLetter = key[keyCurrent]
    print(keyLetter)
    x -= 1
"""    

alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
for number in range(len(phrase)):
    number = int(number)
    letter = phrase[number]
    if letter in alphabet:
        number = ord(letter) - 97

        keyCurrent = defineKeyCurrent(keyCurrent, key)
        letterel = key[keyCurrent]
        # FOR TESTING KEYWORD print("keyletter:", keyLetter)
        shift = ord(letterel) - 97
        if endecode == "e":
            number = number + shift
        elif endecode == "d":
            number = number - shift
        number = number % 26
        NewLetter = chr(number + 97)
        NewPhrase = NewPhrase + NewLetter
    else:
        NewPhrase = NewPhrase + letter

print("-----------------")
if endecode == "e":
    print("The encoded message is:")
elif endecode == "d":
    print("The decoded message is:")

print(NewPhrase)
if endecode == "e":
    myFile = open ("encoded message.txt", "wt")
    myFile.write(NewPhrase)
    myFile.close()
elif endecode == "d":
    myFile = open ("plaintext.txt", "wt")
    myFile.write(NewPhrase)
    myFile.close()
input()





