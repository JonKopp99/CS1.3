import resource
import platform
from hashtable import HashTable
"""
You have a carrier route list with 100,000 (100K) entries (in arbitrary order)
and a list of 1000 phone numbers. How can you operationalize the route cost
lookup problem?

1)Seperate 1000 phone#'s into array'
2)Split the routes into a dictionary for constant time Searching
    -When splitting seperate by comma
    -Check if newValue < oldVal only update if its less
3)Loop through len([phone#s])substringing last # off every iteraiton
4)If []results ->helper function to find lowest route cost
"""
def splitIntoArray(path):
    with open(path) as file:
        lines = file.read().splitlines()
    return lines
#O(n)where n is the length of the words
def splitIntoHash(path):
    with open(path) as file:
        lines = file.read().splitlines()
    theHash = HashTable()
    for line in lines:
        mylist = line.split(',')
        if(theHash.contains(mylist[0])):
            oldVal = theHash.get(mylist[0])
            if(oldVal > mylist[1]):
                theHash.set(mylist[0], mylist[1])
        else:
             theHash.set(mylist[0], mylist[1])
    return theHash

#Averags O(m * n) where M is the length of the array and n is length of the phone number
def findMatches(pn, theDict):
    for phoneNum in pn:
        ctr = len(phoneNum) - 1
        loop = True
        while(loop):
            s = phoneNum[0:ctr]
            #print(s)
            if(s in theDict.keys()):
                loop = False
                print(theDict[s])
            ctr -= 1
            if(ctr <= 1):
                loop = False



if __name__ == '__main__':
    theArray = splitIntoArray('pn100.txt')
    theHash = splitIntoHash('rc100.txt')
    #print(theDict)
    #print(findMatches(theArray, theDict))
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    usage=round(usage/float(1<<20),2)

# print memory usage
    print("Memory Usage: {} mb.".format(usage))
