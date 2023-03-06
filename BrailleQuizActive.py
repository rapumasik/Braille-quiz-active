import random
from rich import print as rPrint
import winsound
import msvcrt
import pyttsx3

brailleAlphabet_dict = {
        'a': '100000',
        'b': '101000',
        'c': '110000',
        'd': '110100',
        'e': '100100',
        'f': '111000',
        'g': '111100',
        'h': '101100',
        'i': '011000',
        'j': '011100',
        'k': '100010',
        'l': '101010',
        'm': '110010',
        'n': '110110',
        'o': '100110',
        'p': '111010',
        'q': '111110',
        'r': '101110',
        's': '011010',
        't': '011110',
        'u': '100011',
        'v': '101011',
        'w': '011101',
        'x': '110011',
        'y': '110111',
        'z': '100111'
    }

brailleAlphabet_dict = {
        'a': '10 00 00',
        'b': '10 10 00',
        'c': '11 00 00',
        'd': '11 01 00',
        'e': '10 01 00',
        'f': '11 10 00',
        'g': '11 11 00',
        'h': '10 11 00',
        # 'i': '01 01 00',
        'i': '01 10 00',
        'j': '01 11 00',
        'k': '10 00 10',
        'l': '10 10 10',
        'm': '11 00 10',
        'n': '11 01 10',
        'o': '10 01 10',
        'p': '11 10 10',
        'q': '11 11 10',
        'r': '10 11 10',
        # 's': '01 01 10',
        's': '01 10 10',
        't': '01 11 10',
        'u': '10 00 11',
        'v': '10 10 11',
        # 'w': '01 01 11',
        'w': '01 11 01',
        'x': '11 00 11',
        'y': '11 01 11',
        'z': '10 01 11'
    }


test = """11
11
11"""

def isKosherFormat(inputString):
	kosherStatus = ""
	# if set(inputString).issubset({'\n', '0', '1'}) == False:
	if set(inputString).issubset({" ", "0", "1"}) == False:
			# future: either change dataformat or count amount of spaces
		print("disallowed character used")
		kosherStatus = False
	if len(inputString) != 8:
		print("incorrect amount of characters")
		kosherStatus = False
	if kosherStatus != False:
		kosherStatus = True
	return kosherStatus
# end of def
# isKosherFormat(test)
# isKosherFormat(threeLineInput(" "))


def threeLineInput(outputSeparator):
	typedInput_p1 = input()
	# typedInput2 = typedInput1 + " " + input()
	# print(f"{typedInput2=}")
	typedInput_p2 = input()
	typedInput_p3 = input()
	typedInput_complete = (
					typedInput_p1
					+ " "
					+ typedInput_p2
					+ " "
					+ typedInput_p3
					)
	# print(f"{typedInput_complete=}")
	return typedInput_complete
# end of def
# threeLineInput(" ")




# list of colours: https://rich.readthedocs.io/en/latest/appendix/colors.html#appendix-colors
def colourPrint(input, colour):
	# rPrint(f"[{colour}]{str(input)}[/{colour}]")
	rPrint(f"[{colour}]{str(input)}[/{colour}]")

# end of def
# colourPrint(x, "red")


def splitPrint(inputString):
	listified = inputString.split(" ")
	listified = [f"█ {line} █" for line in listified]
	# print(listified)
	outputString = "\n".join(listified)
	# print(outputString)
	colourPrint(outputString, "green")
	# print(outputString.splitlines())
# end of def
# splitPrint("ab cd ef")
# splitPrint("10 01 11")



def isEven(integer):	# used in charByCharInput
	if integer % 2 == 0:
		return True
	else:
		return False
# end of def
# isEven(0)
# isEven(1)
# isEven(4)


def charByCharInput(outputSeparator):
	typedInput_list = []
	for number in range(1, 6+1):
		# typedInput_list.append(msvcrt.getch().decode("utf-8"))
		currentInputCharacter = msvcrt.getch().decode("utf-8")
		if currentInputCharacter == "x":
			return "end"
		typedInput_list.append(currentInputCharacter)
		if isEven(number) == False:
			print(currentInputCharacter, end="")
		else:
			print(currentInputCharacter)
	"""
	typedInput_p1 = msvcrt.getch().decode("utf-8")
	typedInput_p2 = msvcrt.getch().decode("utf-8")
	typedInput_p3 = msvcrt.getch().decode("utf-8")
	typedInput_p4 = msvcrt.getch().decode("utf-8")
	typedInput_p5 = msvcrt.getch().decode("utf-8")
	typedInput_p6 = msvcrt.getch().decode("utf-8")
	"""
	#
	typedInput_complete = (
					typedInput_list[0] + typedInput_list[1]
					+ outputSeparator
					+ typedInput_list[2] + typedInput_list[3]
					+ outputSeparator
					+ typedInput_list[4] + typedInput_list[5]
					)
	print(f"{typedInput_complete=}")
	return typedInput_complete
# end of def
# charByCharInput(" ")

natoAlphabet_string = """	# for pronounce()	# possibly use respelling: https://en.wikipedia.org/wiki/NATO_phonetic_alphabet
Alfa
Bravo
Charlie
Delta
Echo
Foxtrot
Golf
Hotel
India
Juliett
Kilo
Lima
Mike
November
Oscar
Papa
Quebec
Romeo
Sierra
Tango
Uniform
Victor
Whiskey
X-ray
Yankee
Zulu
"""

natoAlphabet_dict = {}	# for pronounced()
for word in natoAlphabet_string.strip("\n").splitlines():
	# print(word)
	# print(word.lower())
	# print(word[0])
	# print(word[0].lower())
	# print()
	natoAlphabet_dict[word[0].lower()] = word
natoAlphabet_dict["x"]  = "ECKS ray"
# print(natoAlphabet_dict)

def pronounce(inputString, codeWords=False):
	pyttsx3_engine = pyttsx3.init()
	if codeWords == False:
		pyttsx3_engine.say(inputString.upper())
	else:
		phrase_string = inputString.upper() + ", as in" + natoAlphabet_dict[inputString]
		pyttsx3_engine.say(phrase_string)
	pyttsx3_engine.runAndWait()
# end of def
# pronounce("yes")
# pronounce("x", codeWords=True)

print("type in the dots or blanks of the letter using 1 and 0.")
print("in this order:")
print("12")
print("34")
print("56")
print("you don't have to press 'return' to get to the next line.")
print("press 'x' at any point to end the quiz.")
print("---")
print()
mistakeCount = 0
# for letter in list(brailleAlphabet_dict.keys()):
# for letter in random.sample(list(brailleAlphabet_dict.keys()), len(brailleAlphabet_dict))[:4]:
for letter in random.sample(list(brailleAlphabet_dict.keys()), len(brailleAlphabet_dict)):
	print(letter)
	pronounce(letter, codeWords=True)
	print()
	# typedInput = input()
	# typedInput = threeLineInput(" ")
	typedInput = charByCharInput(" ")
	print()
	if typedInput == brailleAlphabet_dict[letter]:
		print("correct")
	elif typedInput == "end":
		print("you cut the quiz short.")
		break
	elif	isKosherFormat(typedInput) == False:	# future: give another chance
			winsound.Beep(600, 50)
			winsound.Beep(500, 50)
			print("your input was not in the proper format")
			mistakeCount += 1
			print("solution:")
			splitPrint(brailleAlphabet_dict[letter])
	else:
		winsound.Beep(600, 50)
		winsound.Beep(500, 50)
		# winsound.Beep(400, 50)
		print(">>> incorrect <<<")
		print()
		mistakeCount += 1
		# print("solution:", brailleAlphabet_dict[letter])
		print("solution:")
		splitPrint(brailleAlphabet_dict[letter])
	print()
	print("---")
	print()
# end of loop
print("you made", mistakeCount, "mistakes")
input("press 'return' to close")
