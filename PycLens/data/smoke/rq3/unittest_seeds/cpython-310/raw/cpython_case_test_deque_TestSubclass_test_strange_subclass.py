# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestSubclass_test_strange_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X(deque):

        def __iter__(self):
            return iter([])
    d1 = X([1, 2, 3])
    d2 = X([4, 5, 6])
    d1 == d2
