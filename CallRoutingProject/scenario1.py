"""
You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a
single phone number. How quickly can you find the cost of calling this number?

1)Split the routes into a dictionary for constant time Searching
    -When splitting seperate by comma
    -Check if newValue < oldVal only update if its less
2)Loop through len(phone#)substringing last # off every iteraiton
3)If []results ->helper function to find lowest route cost
"""
#O(n)where n is the length of the words
def splitIntoDict(path):
    with open(path) as file:
        lines = file.read().splitlines()
    theDict = {}
    for line in lines:
        mylist = line.split(',')
        if(mylist[0] in theDict.keys()):
            oldVal = theDict[mylist[0]]
            if(oldVal > mylist[1]):
                theDict[mylist[0]] = mylist[1]
        else:
             theDict[mylist[0]] = mylist[1]
    return theDict

#O(1) Best case if the phone number is a route
#O(n) N being lenth of phonenumber string if there are not matches for routes
def findMatches(pn, theDict):
    ctr = len(pn) - 1
    #print(theDict.keys())
    while(ctr > 1):
        s = pn[0:ctr]
        print(s)
        if(s in theDict.keys()):
            return theDict[s]
        ctr -= 1
    return None



if __name__ == '__main__':
    theDict = splitIntoDict('rc100.txt')
    #print(theDict)
    print(findMatches("+18017154269", theDict))
