

class set(object):
    def __init__(self, elements = None):
        self.size = 0
        self.list = []
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
        if(sef.contains(item)):
            return False
        self.list.append(item)
        return True
    def remove(self, item):
            if self.contains(item):
                self.list.remove(item)
                self.size -= 1
                return True
            return False

if __name__ == '__main__':
    testAr = [1,3,5,2,4]
    theSet = set(testAr)
    print(theSet.length())
    assert theSet.length() == 5
    theSet.remove(3)
    print(theSet.contains(3))
    print(theSet.length())
    assert theSet.length() == 4
