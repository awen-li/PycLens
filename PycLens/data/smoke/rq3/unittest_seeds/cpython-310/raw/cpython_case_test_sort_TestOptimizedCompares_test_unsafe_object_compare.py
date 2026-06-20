# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sort.py
# case: TestOptimizedCompares_test_unsafe_object_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class WackyComparator(int):

        def __lt__(self, other):
            elem.__class__ = WackyList2
            return int.__lt__(self, other)

    class WackyList1(list):
        pass

    class WackyList2(list):

        def __lt__(self, other):
            raise ValueError
    L = [WackyList1([WackyComparator(i), i]) for i in range(10)]
    elem = L[-1]
    with self.assertRaises(ValueError):
        L.sort()
    L = [WackyList1([WackyComparator(i), i]) for i in range(10)]
    elem = L[-1]
    with self.assertRaises(ValueError):
        [(x,) for x in L].sort()

    class PointlessComparator:

        def __lt__(self, other):
            return NotImplemented
    L = [PointlessComparator(), PointlessComparator()]
    self.assertRaises(TypeError, L.sort)
    self.assertRaises(TypeError, [(x,) for x in L].sort)
    lists = [list(range(100)) + [1 << 70], [str(x) for x in range(100)] + ['\uffff'], [bytes(x) for x in range(100)], [cmp_to_key(lambda x, y: x < y)(x) for x in range(100)]]
    for L in lists:
        check_against_PyObject_RichCompareBool(self, L)
