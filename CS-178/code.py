import copy

def ca45(caVector):
    # This function runs the CA 45 rule on the input vector caVector

    vectorPrintString="Vector 0: " +repr(caVector)
    print vectorPrintString

    for vectorNum in range (1,17): #we want 16 vectors
        
        oldVector=copy.deepcopy(caVector); #store the old vector values
    
        vectorIndexPrintString="Vector "+repr(vectorNum)+":"
        print (vectorIndexPrintString),
        
        for vectorIndex in range (0,17):
            #this will iterate through the elements in the vector, updating the
            
            p=(vectorIndex-1)%17 #wrap around
            q=vectorIndex%17
            r=(vectorIndex+1)%17
            
            
            caVector[vectorIndex]=(1+oldVector[p]+oldVector[r]+(oldVector[q]*oldVector[r]))%2
            
            print (repr(caVector[vectorIndex])),
        
        print "\n"
    return

#call ca45:

inputVector=([0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
ca45(inputVector)