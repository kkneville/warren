import random


def newName():
	letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	
	vowels = ["a", "ai", "aa", "au", "ay", "e", "ee", "ei", "eo", "ey", "i", "ie", "ia", "o", "oo", "oa", "oy", "u", "ui", "ue", "y", "ya", "ye", "yi", "yue", "yau"]
	
	consonants = ["b", "br", "bl", "c", "cr", "d", "dr", "dl", "dt", "f", "fl", "fr", "g", "gh", "h", "hs", "j", "jh", "jhr", "k", "kl", "kr", "kh", "khr", "khl", "kt", "l", "ll", "m", "mm", "n", "mn", "mh", "p", "ph", "pl", "pr", "py", "q", "qh", "r", "rr", "s", "sl", "sk", "ss", "t", "tt", "tr", "tl", "v", "vr", "vl", "w", "wh", "x", "xh", "y", "z", "zr", "zl", "zh"]

	name = ""
	letter_type = ""
	length = random.randint(3, 6)

	for each in length:
		if name.length < 1:
			letter_type = random.choice("vowel", "consonant")
			
		if letter_type == "vowel":
			name.append(vowels[random.randint(0, vowels.length)])
			letter_type = "consonant"
		else :
			name.append(consonants[random.randint(0, consonants.length)])
			letter_type = "vowel"

		return name

		