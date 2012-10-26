#!/usr/bin/python

from sys import argv
from pprint import pprint

def getPalindrome(inString):
	seenIndices = {}
	print palindrominate(inString, 0, seenIndices)

def palindrominate(inString, offset, seenIndices):
	if(len(inString) == 0):
		return ""

	longest = ""
	for i in range(0,len(inString)):
		curLetter = inString[i]
		farthestIndex = inString.rindex(curLetter);
		index = str(i+offset)+str(farthestIndex+offset)
		pal = ""

		if(index in seenIndices):
			pal = seenIndices[index]
		elif(farthestIndex == i):
			seenIndices[index] = curLetter
			pal = curLetter
		else:
			pal = curLetter + palindrominate(inString[i+1:farthestIndex], i + 1,  seenIndices) + curLetter
			seenIndices[index] = pal
		
		if(len(pal) > len(longest)):
			longest = pal
	return longest

getPalindrome(argv[1])
