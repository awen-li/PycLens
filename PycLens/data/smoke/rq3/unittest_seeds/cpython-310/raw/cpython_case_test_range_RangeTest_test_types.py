# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIn(1.0, range(3))
    self.assertIn(True, range(3))
    self.assertIn(1 + 0j, range(3))
    self.assertIn(ALWAYS_EQ, range(3))

    class C2:

        def __int__(self):
            return 1

        def __index__(self):
            return 1
    self.assertNotIn(C2(), range(3))
    self.assertIn(int(C2()), range(3))

    class C3(int):

        def __eq__(self, other):
            return True
    self.assertIn(C3(11), range(10))
    self.assertIn(C3(11), list(range(10)))
