# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_richcmp.py
# case: MiscTest_test_misbehavin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Misb:

        def __lt__(self_, other):
            return 0

        def __gt__(self_, other):
            return 0

        def __eq__(self_, other):
            return 0

        def __le__(self_, other):
            self.fail("This shouldn't happen")

        def __ge__(self_, other):
            self.fail("This shouldn't happen")

        def __ne__(self_, other):
            self.fail("This shouldn't happen")
    a = Misb()
    b = Misb()
    self.assertEqual(a < b, 0)
    self.assertEqual(a == b, 0)
    self.assertEqual(a > b, 0)
