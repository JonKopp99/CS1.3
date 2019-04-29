#O(n) becasue we iterate through the array of words but looking
#through the set is constant time
def redact_words(words, banned_words):
    newAr = []
    bannedWords = set(banned_words)
    for word in words:
        if(word not in bannedWords):
            newAr.append(word)
    return newAr


if __name__ == '__main__':
    ar1 = ["i", "like", "dogs"]
    ar2 = ["dogs","cats"]
    assert redact_words(ar1,ar2) == ["i","like"]

    ar3 = ["i", "like", "dogs", "and", "cats"]
    ar4 = ["dogs","cats"]
    assert redact_words(ar3,ar4) == ["i","like","and"]

    ar5 = ["i", "like", "dogs", "and", "cats","and","hamsters"]
    ar6 = ["dogs","cats","and","hamsters"]
    assert redact_words(ar5,ar6) == ["i","like"]
