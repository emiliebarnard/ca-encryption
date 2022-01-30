#!/usr/bin/env python3

#(c) Emilie Menard Barnard, UC Regents
#Project for Professor Koc's CS178 at UC Santa Barbara, Winter 2013

#CELLULAR AUTOMATA ENCRYPTION

import copy
import cgi

print("Content-type: text/html\n")

#The general rule lookup function helpers:

#This is our 8-bit lookup table:
lookupTable=([0,0,0,0,0,0,0,0])


#This function creates the lookup table based on the inputted rule number:
def createLookupTable(ruleNumber):
	ruleNumber=(bin(ruleNumber))
	
	ruleNumberIndex=len(ruleNumber)-1
	tableIndex=len(lookupTable)-1
	
	# Some parsing
	while ruleNumber[ruleNumberIndex]!='b':
		lookupTable[tableIndex]=int(ruleNumber[ruleNumberIndex])
		ruleNumberIndex=ruleNumberIndex-1
		tableIndex=tableIndex-1

############################################

#My CA function that performs the encryption:
def ca(caVector, ruleNumber, numSteps):

    for vectorNum in range (0,numSteps+1): #We will produce numSteps many new vectors
        
        oldVector=copy.deepcopy(caVector); #Store the old vector values
        
        #This will iterate through the elements in the vector and update the values
        for vectorIndex in range(len(caVector)): 
            
            p=(vectorIndex-1)%(len(inputVector)) #wrap around for boundary cases
            q=vectorIndex%(len(inputVector))
            r=(vectorIndex+1)%(len(inputVector))
            
			# This will generate the new cell using the lookup table:
            decRep=oldVector[r]+2*oldVector[q]+4*oldVector[p]
            caVector[vectorIndex]=lookupTable[(len(lookupTable)-1)-decRep]
            
            print(repr(caVector[vectorIndex]), end="")
            
        if (vectorNum<numSteps):    
        	print()

    return

############################################

#Call the code:

# JS interaction:
try:
	form=cgi.FieldStorage()
	#print("here")
	rule=(int(form.getfirst("rule")))%256
	#print("here1")
	numSteps=int(form.getfirst("numSteps"))
	#numSteps = 10
	inputVector=form.getfirst("inputVector").split(" ")
	#inputVector = "0 0 0 0 0 0 0 0 0".split(" ")

	inputVector=[ int(x) for x in inputVector]
	
	createLookupTable(rule)
	ca(inputVector, rule, numSteps)

# For error debugging:
except Exception as fail:
	print("Failure: " + repr(fail))
