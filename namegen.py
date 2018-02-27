import random


def newName(num):
	letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	
	vowels = ["a", "ai", "aa", "au", "ay", "e", "ee", "ei", "eo", "ey", "i", "ie", "ia", "o", "oo", "oa", "oy", "u", "ui", "ue", "y", "ya", "ye", "yi", "yue", "yau"]
	
	consonants = ["b", "br", "bl", "c", "cr", "d", "dr", "dl", "dt", "f", "fl", "fr", "g", "gh", "h", "hs", "j", "jh", "jhr", "k", "kl", "kr", "kh", "khr", "khl", "kt", "l", "ll", "m", "mm", "n", "mn", "mh", "p", "ph", "pl", "pr", "py", "q", "qh", "r", "rr", "s", "sl", "sk", "ss", "t", "tt", "tr", "tl", "v", "vr", "vl", "w", "wh", "x", "xh", "y", "z", "zr", "zl", "zh"]

	names = []
	name = ""
	letter_type = -1
	length = random.randint(3, 7)

	for one in range(0, num):
		for each in range(0, length):
			if len(name) < 1:
				letter_type = random.randint(0,2)
				
			if letter_type == 0:
				name += vowels[random.randint(0, len(vowels)-1)]
				letter_type = 1
				continue 
				
			elif letter_type == 1:
				name += consonants[random.randint(0, len(consonants)-1)]
				letter_type = 0

		names.append(name)
		name = ""
	return names	
			

test = newName(5)
print (test)


def vikingName(num):
	pref = ["Snor", "Skar", "Mar", "Jarl", "Grim", "Grip", "Kam", "Krak", "Krav", "Marl", "Agon", "Arnar", "Ibar", "Jung"]
		
