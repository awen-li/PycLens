# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_MutableSequence_mixins

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MutableSequenceSubclass(MutableSequence):

        def __init__(self):
            self.lst = []

        def __setitem__(self, index, value):
            self.lst[index] = value

        def __getitem__(self, index):
            return self.lst[index]

        def __len__(self):
            return len(self.lst)

        def __delitem__(self, index):
            del self.lst[index]

        def insert(self, index, value):
            self.lst.insert(index, value)
    mss = MutableSequenceSubclass()
    mss.append(0)
    mss.extend((1, 2, 3, 4))
    self.assertEqual(len(mss), 5)
    self.assertEqual(mss[3], 3)
    mss.reverse()
    self.assertEqual(mss[3], 1)
    mss.pop()
    self.assertEqual(len(mss), 4)
    mss.remove(3)
    self.assertEqual(len(mss), 3)
    mss += (10, 20, 30)
    self.assertEqual(len(mss), 6)
    self.assertEqual(mss[-1], 30)
    mss.clear()
    self.assertEqual(len(mss), 0)
    items = 'ABCD'
    mss2 = MutableSequenceSubclass()
    mss2.extend(items + items)
    mss.clear()
    mss.extend(items)
    mss.extend(mss)
    self.assertEqual(len(mss), len(mss2))
    self.assertEqual(list(mss), list(mss2))
