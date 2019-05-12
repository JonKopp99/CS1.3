from set import set
import unittest

class setTest(unittest.TestCase):

    def testAddAndSize(self):
        print("Testing add and size!")
        testAr = [1,3,5,2,4]
        theSet = set(testAr)
        assert theSet.size == 5
        theSet.add(7)
        assert theSet.size == 6
        theSet.add(2)
        assert theSet.size == 6
        theSet.add(8)
        assert theSet.size == 7

    def testRemoveAndContains(self):
        print("Testing remove and contains")
        testAr = ["a", "b", "c", "d", "e", "f", "g"]
        theSet = set(testAr)
        assert theSet.size == 7
        assert theSet.contains("a") == True
        assert theSet.remove("a") == True
        assert theSet.contains("a") == False
        assert theSet.remove("b") == True
        assert theSet.contains("b") == False
        assert theSet.remove("c") == True
        assert theSet.contains("c") == False
        assert theSet.remove("d") == True
        assert theSet.contains("d") == False

    def testIntersection(self):
        print("Testing interseciton")
        theSet1 = set([1,3,5,2,4])
        theSet2 = set([1,3,5])
        assert theSet1.intersection(theSet2).list == [1,3,5]
        theSet1 = set(["a", "b", "c", "d", "e", "f", "g"])
        theSet2 = set(["a", "b", "c", "d", "e", "f", "g"])
        assert theSet1.intersection(theSet2).list == ["a", "b", "c", "d", "e", "f", "g"]
        assert theSet2.remove("b") == True
        assert theSet1.intersection(theSet2).list == ["a", "c", "d", "e", "f", "g"]

    def testUnion(self):
        print("Testing union!")
        theSet1 = set([2,4])
        theSet2 = set([1,3,5])
        assert theSet1.union(theSet2).list == [1,3,5,2,4]
        theSet1 = set(["a", "b", "c"])
        theSet2 = set(["d", "e", "f", "g"])
        assert theSet1.union(theSet2).list == ["d", "e", "f", "g", "a", "b", "c"]
        assert theSet1.remove("c") == True
        assert theSet1.union(theSet2).list == ["d", "e", "f", "g", "a", "b"]

    def testDifference(self):
        print("Testing difference!")
        theSet1 = set([1,3,5,2,4])
        theSet2 = set([1,3,5])
        assert theSet2.difference(theSet1).list == [2,4]
        theSet1 = set(["a", "b", "c"])
        theSet2 = set(["a", "b", "c", "g"])
        assert theSet2.difference(theSet1).list == ["g"]
        theSet1 = set([1,3,5,2])
        theSet2 = set([1,3,5])
        assert theSet2.difference(theSet1).list == [2]
        theSet1 = set(["a", "b", "c"])
        theSet2 = set(["a", "b", "c", "h"])
        assert theSet2.difference(theSet1).list == ["h"]

    def testIsSubset(self):
        print("Testing is_subset!")
        theSet1 = set([1,3,5,2,4])
        theSet2 = set([1,3,5])
        assert theSet2.is_subset(theSet1) == True
        assert theSet1.is_subset(theSet2) == False
        theSet1 = set(["a", "b", "c", "d", "e", "f", "g"])
        theSet2 = set(["a", "b", "c", "d", "e"])
        assert theSet2.is_subset(theSet1) == True
        assert theSet1.is_subset(theSet2) == False
        theSet1 = set(["jon", "is", "the", "coolest"])
        theSet2 = set(["jon", "is", "coolest"])
        assert theSet2.is_subset(theSet1) == True
        assert theSet1.is_subset(theSet2) == False

if __name__ == '__main__':
    unittest.main()
