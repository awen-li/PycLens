# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_isinstance.py
# case: TestIsInstanceIsSubclass_test_infinite_recursion_in_bases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        @property
        def __bases__(self):
            return self.__bases__
    with support.infinite_recursion():
        self.assertRaises(RecursionError, issubclass, X(), int)
        self.assertRaises(RecursionError, issubclass, int, X())
        self.assertRaises(RecursionError, isinstance, 1, X())
