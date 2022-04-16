print("""
╔═════════════════════════════╗
║ Welcome to my caeser cipher ║
╚═════════════════════════════╝
""")
NewPhrase = ""
shift = 0
print("enter phrase to encode/decode")
phrase = str(input())
print()
print("Enter shift of letter (- to go backward)")
shift = int(input())

def defineLetter(number):
    if number == 1:
        newL = "a"
    elif number == 2:
        newL = "b"
    elif number == 3:
        newL = "c"
    elif number == 4:
        newL = "d"
    elif number == 5:
        newL = "e"
    elif number == 6:
        newL = "f"
    elif number == 7:
        newL = "g"
    elif number == 8:
        newL = "h"
    elif number == 9:
        newL = "i"
    elif number == 10:
        newL = "j"
    elif number == 11:
        newL = "k"
    elif number == 12:
        newL = "l"
    elif number == 13:
        newL = "m"
    elif number == 14:
        newL = "n"
    elif number == 15:
        newL = "o"
    elif number == 16:
        newL = "p"
    elif number == 17:
        newL = "q"
    elif number == 18:
        newL = "r"
    elif number == 19:
        newL = "s"
    elif number == 20:
        newL = "t"
    elif number == 21:
        newL = "u"
    elif number == 22:
        newL = "v"
    elif number == 23:
        newL = "w"
    elif number == 24:
        newL = "x"
    elif number == 25:
        newL = "y"
    elif number == 0:
        newL = "z"
    return(newL)

numbers = len(phrase)
for number in range(numbers):
    int(number)
    letter = phrase[number]
    letter = letter.lower()
    if letter != " ":
        number = ord(letter) -97
        
        number = number + shift
        number = number % 26
        NewLetter = chr(number + 97)
        NewPhrase = NewPhrase + NewLetter
    if letter == " ":
        NewPhrase = NewPhrase + " "

print()
print("The encoded message is:")
print(NewPhrase)
input()
