# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_list.py
# case: ListTest_test_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lst = [4, 5, 6, 7]
    n = int((sys.maxsize * 2 + 2) // len(lst))

    def mul(a, b):
        return a * b

    def imul(a, b):
        a *= b
    self.assertRaises((MemoryError, OverflowError), mul, lst, n)
    self.assertRaises((MemoryError, OverflowError), imul, lst, n)
