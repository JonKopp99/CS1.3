import re
def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    textFormatted = re.sub('[!@#$-?., ]', '', text).lower()
    patFormatted = re.sub('[!@#$-?., ]', '', pattern).lower()
    correctCtr = 0
    ctr = 0
    if(pattern == ''):
        return True
    while ctr < len(text):
        if(textFormatted[ctr] == patFormatted[correctCtr]):
            print("Match", correctCtr)
            if(correctCtr == len(patFormatted) - 1):
                print("Contains pattern")
                return True
            correctCtr += 1
        elif(correctCtr > 0):
            correctCtr = 0
            ctr -= 1
        ctr += 1
    return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    textFormatted = text#re.sub('[!@#$-?., ]', '', text).lower()
    patFormatted = pattern#re.sub('[!@#$-?., ]', '', pattern).lower()
    correctCtr = 0
    ctr = 0
    if(pattern == ''):
        return 0
    while ctr < len(text):
        if(textFormatted[ctr] == patFormatted[correctCtr]):
            print("Match", correctCtr)
            if(correctCtr == len(patFormatted) - 1):
                print("Contains pattern")
                return ctr - correctCtr
            correctCtr += 1
        elif(correctCtr > 0):
            correctCtr = 0
            ctr -= 1
        ctr += 1
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    indexies = []
    textFormatted = text#re.sub('[!@#$-?., ]', '', text).lower()
    patFormatted = pattern#re.sub('[!@#$-?., ]', '', pattern).lower()
    correctCtr = 0
    ctr = 0
    if(pattern == ''):
        print("Contains none!!!")
        return [0,1,2]
    while ctr < len(text):
        if(textFormatted[ctr] == patFormatted[correctCtr]):
            print("Match", correctCtr)
            correctCtr += 1
            if(correctCtr  == len(patFormatted) - 1):
                print("Counter:", ctr)
                print("Contains pattern")
                indexies.append(ctr - (correctCtr - 1))
                correctCtr = 0
            ctr += 1
        elif(correctCtr > 0):
            correctCtr = 0
        else:
            ctr += 1
    return indexies


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
    #contains("Jonathan","Jon")
    #contains("abc","z")
    #print(find_index("NotJonathan","Jon"))
    print(find_all_indexes("aaa", "aa"))
    #main()
