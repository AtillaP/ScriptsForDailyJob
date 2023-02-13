class SigFunc:
    # Constructor for reading from excel
    def __init__(self, name, message):
        self.name = name
        self.message = message
        self.message = message
        self.signalDefinition = []
        self.outputFile = "NA"
        self.indexToDelete = []
    def setSignalDefinition(self, lines, index):
        lineCount, brackets = 0, -1
        functionIndex = index
        # Collect comments before function
        while ("/**" not in lines[functionIndex] or lineCount > 20):
            functionIndex -= 1
            lineCount += 1
        # If the comments would not been found, start collect from the functionname
        if lineCount >= 20:
            functionIndex = index
        lineCount = 0
        # Collect function definition itself
        for line in lines[functionIndex:]:
            # Check for the opening and ending boundary of the function
            # based on the amount of the brackets
            opBr = line.count('{')
            clsBr = line.count('}')
            if "{" in line and brackets == -1:
                brackets = 1
                opBr -= 1
            brackets += (opBr - clsBr)
            lineCount += 1
            # Append line to the definition of the function
            self.signalDefinition.append(line)
            # Collect indexes of the sourceList, which concerns to the signal
            self.indexToDelete.append(functionIndex)
            functionIndex += 1
            # End of function definition:
            #    1. closing bracjets has been found
            #    2. 250 lines exceeded
            if brackets == 0 or lineCount == 250:
                break
        self.signalDefinition.append(lines[functionIndex])
    def setOutPutFile(self, path):
        if self.message != "UNKNOWN":
            self.outputFile = f'{path}{self.message}.txt'
    def getName(self):
        return self.name
    def getMessage(self):
        return self.message
    def getOutputFile(self):
        return self.outputFile
    def getLengthOfSignalCode(self):
        return len(self.signalDefinition)
    def getIndexesToDelete(self):
        return self.indexToDelete
    def getLengthOfIndexToDelete(self):
        return len(self.indexToDelete)
    def getSignalDefitnition(self):
        return self.signalDefinition
    def printSignalToConsole(self):
        if len(self.signalDefinition) == 0:
            return "NA"
        else:
            for i in range(0, len(self.signalDefinition)):
                print(self.signalDefinition[i][:-1])
    def printSignalToFile(self):
        if len(self.signalDefinition) == 0 or self.outputFile == "NA" or self.message == "UNKNOWN":
            return "NA"
        else:
            with open(self.outputFile, 'a') as text_file:
                for line in self.signalDefinition:
                    text_file.write(f'{line}')
                text_file.close()
    def printIndexes(self):
        print(self.name + ":")
        if len(self.signalDefinition) != 0:
            for i in self.indexToDelete:
                print(i)
        else:
            print("NA")
        print(20*"-")