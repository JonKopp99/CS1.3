

class set(object):
    def __init__(self, elements = None):
        self.size = 0
        self.list = []
        if(elements != None):
            for item in elements:
                self.size += 1
                self.list.append(item)

    def length(self):
        return self.size

    def is_empty(self):
        return self.size < 1

    def contains(self, item):
        for i in self.list:
            if i == item:
                return True
        return False
    def add(self, item):
        if(self.contains(item)):
            return False
        self.list.append(item)
        return True
    def remove(self, item):
            if self.contains(item):
                self.list.remove(item)
                self.size -= 1
                return True
            return False
    def intersection(self, otherSet):
        newSet = set()

        if(otherSet.length() >= self.length()):
            smallSet = self
            bigSet = otherSet
        else:
            smallSet = otherSet
            bigSet = self

        for item in smallSet.list:
            if bigSet.contains(item):
                newSet.add(item)
        return newSet


if __name__ == '__main__':
    testAr = [1,3,5,2,4]
    theSet = set(testAr)
    print(theSet.length())
    assert theSet.length() == 5
    theSet.remove(3)
    print(theSet.contains(3))
    print(theSet.length())
    assert theSet.length() == 4

    testAr2 = [1,3,5]
    theSet2 = set(testAr2)
    newIntSet = theSet.intersection(theSet2)
    print(newIntSet.list)
    assert newIntSet.list == [1, 5]
