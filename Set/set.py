

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
        self.size += 1
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


    def union(self, otherSet):
        newSet = set()

        if(otherSet.length() >= self.length()):
            smallSet = self
            bigSet = otherSet
        else:
            smallSet = otherSet
            bigSet = self
        newSet.list += bigSet.list
        for i in smallSet.list:
            if(newSet.contains(i) == False):
                newSet.add(i)
        return newSet

    def difference(self, otherSet):
        newSet = set()

        for i in self.list:
            if(otherSet.contains(i) == False):
                newSet.add(i)
        for i in otherSet.list:
            if(self.contains(i) == False):
                newSet.add(i)
        return newSet


    def is_subset(self, otherset):
        for i in self.list:
            if(otherset.contains(i) == False):
                return False
        return True

# if __name__ == '__main__':
#     #Basic functions test
#     testAr = [1,3,5,2,4]
#     theSet = set(testAr)
#     print(theSet.length())
#     assert theSet.length() == 5
#     theSet.remove(3)
#     print("Does set contain 3?: " , theSet.contains(3))
#     print(theSet.length())
#     assert theSet.length() == 4
#
#     #Intersection test
#     testAr2 = [1,3,5]
#     theSet2 = set(testAr2)
#     newIntSet = theSet.intersection(theSet2)
#     print("Intersection of lists: ", newIntSet.list)
#     assert newIntSet.list == [1, 5]
#
#     #Union test
#     newUnionSet = theSet.union(newIntSet)
#     print("Union of the lists: ", newUnionSet.list)
#     assert newUnionSet.list == [1,5,2,4]
#
#     #Difference test
#     set1 = set([1,2,3,4,5])
#     set2 = set([6,7,8,3,10])
#     newDiffSet = set1.difference(set2)
#     print("Diffrence between the two sets: ", newDiffSet.list)
#
#     #Subset test_set_twice_and_get
#     set3 = set([1,2,3])
#     set4 = set([1,4,3,2,5,6])
#     print("Is subset: ", set3.is_subset(set4))
#     print("Is subset: ", set4.is_subset(set3))
