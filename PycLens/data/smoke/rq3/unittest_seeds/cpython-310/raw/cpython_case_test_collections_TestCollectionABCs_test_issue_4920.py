# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_issue_4920

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MySet(MutableSet):
        __slots__ = ['__s']

        def __init__(self, items=None):
            if items is None:
                items = []
            self.__s = set(items)

        def __contains__(self, v):
            return v in self.__s

        def __iter__(self):
            return iter(self.__s)

        def __len__(self):
            return len(self.__s)

        def add(self, v):
            result = v not in self.__s
            self.__s.add(v)
            return result

        def discard(self, v):
            result = v in self.__s
            self.__s.discard(v)
            return result

        def __repr__(self):
            return 'MySet(%s)' % repr(list(self))
    items = [5, 43, 2, 1]
    s = MySet(items)
    r = s.pop()
    self.assertEqual(len(s), len(items) - 1)
    self.assertNotIn(r, s)
    self.assertIn(r, items)
