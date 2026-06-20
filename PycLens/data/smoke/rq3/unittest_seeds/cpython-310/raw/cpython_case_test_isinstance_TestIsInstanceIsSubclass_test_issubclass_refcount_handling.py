# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_isinstance.py
# case: TestIsInstanceIsSubclass_test_issubclass_refcount_handling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        @property
        def __bases__(self):
            return (int,)

    class B:

        def __init__(self):
            self.x = 1

        @property
        def __bases__(self):
            return (A(),)
    self.assertEqual(True, issubclass(B(), int))
