import re
import resource
import platform
def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.Always 0(n)
    where n is the lengh of the string. Because we have to loop through
    each character and find the pattens."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    # textFormatted = re.sub('[!@#$-?., ]', '', text).lower()
    # patFormatted = re.sub('[!@#$-?., ]', '', pattern).lower()
    # correctCtr = 0
    # ctr = 0
    # if(pattern == ''):
    #     return True
    # while ctr < len(text):
    #     if(textFormatted[ctr] == patFormatted[correctCtr]):
    #         print("Match", correctCtr)
    #         if(correctCtr == len(patFormatted) - 1):
    #             print("Contains pattern")
    #             return True
    #         correctCtr += 1
    #     elif(correctCtr > 0):
    #         correctCtr = 0
    #         ctr -= 1
    #     ctr += 1
    # return False
    if(find_index(text,pattern) != None):
        return True
    return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.Always 0(n) where n is the lengh of the string. Because we have to loop
    through
    each character and find the pattens."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # textFormatted = text#re.sub('[!@#$-?., ]', '', text).lower()
    # patFormatted = pattern#re.sub('[!@#$-?., ]', '', pattern).lower()
    # correctCtr = 0
    # ctr = 0
    # if(pattern == ''):
    #     return 0
    # while ctr < len(text):
    #     if(textFormatted[ctr] == patFormatted[correctCtr]):
    #         print("Match", correctCtr)
    #         if(correctCtr == len(patFormatted) - 1):
    #             print("Contains pattern")
    #             return ctr - correctCtr
    #         correctCtr += 1
    #     elif(correctCtr > 0):
    #         correctCtr = 0
    #         ctr -= 1
    #     ctr += 1
    # return None
    theIndexies = find_all_indexes(text, pattern)
    if(len(theIndexies) == 0):
        return None
    return theIndexies[0]


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Always 0(n) where n is the lengh of the string. Because we have to loop through
    each character and find the pattens."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    indexies = []

    #return list of all indexies bc nothingness is in everything :)`]
    if (pattern == ''):
        return list(range(len(text))) #0n

    correctCtr = 0 #01
    ctr = len(pattern) #01
    while ctr <= len(text): #0n
        if text[correctCtr:ctr] == pattern: #01
            indexies.append(correctCtr) #01
        correctCtr += 1 #01
        ctr += 1#01
    return indexies #01



def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    #print(find_all_indexes("aaa", "aa"))
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    usage=round(usage/float(1<<20),2)
    print("Memory Usage: {} mb.".format(usage))
    #main()
    #LET THE TESTING BEGIN!!!

    #TEST CONTAINS
    contains1 = contains("oof", "o")
    assert contains1 == True
    contains2 = contains("Ahhhh", "hhh")
    assert contains2 == True
    contains3 = contains("Ahhhh", "hhhhhhh")
    assert contains3 == False

    #TEST FIND FIRST INDEX
    fi1 = find_index("Jonathan","Jon")
    assert fi1 == 0
    fi2 = find_index("SwoleJon","Jon")
    assert fi2 == 5
    fi2 = find_index("SwoleJohn","Jon")
    assert fi2 == None

    #Test find all indexes
    fai1 = find_all_indexes("JonJonJon", "Jon")
    assert fai1 == [0, 3, 6]
    fai2 = find_all_indexes("NojNojNoj", "")
    assert fai2 == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    fai3 = find_all_indexes("j", "Jon")
    print(fai3)
    assert fai3 == []
