# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_isinstance.py
# case: TestIsInstanceIsSubclass_test_infinite_recursion_via_bases_tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Failure(object):

        def __getattr__(self, attr):
            return (self, None)
    with support.infinite_recursion():
        with self.assertRaises(RecursionError):
            issubclass(Failure(), int)
