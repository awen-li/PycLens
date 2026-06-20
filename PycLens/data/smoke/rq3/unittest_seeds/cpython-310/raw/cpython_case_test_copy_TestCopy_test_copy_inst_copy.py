# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_copy_inst_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __init__(self, foo):
            self.foo = foo

        def __copy__(self):
            return C(self.foo)

        def __eq__(self, other):
            return self.foo == other.foo
    x = C(42)
    self.assertEqual(copy.copy(x), x)
