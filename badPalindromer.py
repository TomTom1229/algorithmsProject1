#!/usr/bin/python

from sys import argv

def getPalindrome(inString):
	print palindrominate(inString)

def palindrominate(inString):
	if(len(inString) == 0):
		return ""

	longest = ""
	for i in range(0,len(inString)-1):
		curLetter = inString[i]
		farthestIndex = inString.rindex(curLetter);
		pal = ""

		if(farthestIndex == i):
			pal = curLetter
		else:
			pal = curLetter + palindrominate(inString[i+1:farthestIndex]) + curLetter
		
		if(len(pal) > len(longest)):
			longest = pal

	return longest

getPalindrome(argv[1])
