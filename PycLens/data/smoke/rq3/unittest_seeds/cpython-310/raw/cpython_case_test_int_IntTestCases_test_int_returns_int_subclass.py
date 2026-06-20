# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntTestCases_test_int_returns_int_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BadIndex:

        def __index__(self):
            return True

    class BadIndex2(int):

        def __index__(self):
            return True

    class BadInt:

        def __int__(self):
            return True

    class BadInt2(int):

        def __int__(self):
            return True

    class TruncReturnsBadIndex:

        def __trunc__(self):
            return BadIndex()

    class TruncReturnsBadInt:

        def __trunc__(self):
            return BadInt()

    class TruncReturnsIntSubclass:

        def __trunc__(self):
            return True
    bad_int = BadIndex()
    with self.assertWarns(DeprecationWarning):
        n = int(bad_int)
    self.assertEqual(n, 1)
    self.assertIs(type(n), int)
    bad_int = BadIndex2()
    n = int(bad_int)
    self.assertEqual(n, 0)
    self.assertIs(type(n), int)
    bad_int = BadInt()
    with self.assertWarns(DeprecationWarning):
        n = int(bad_int)
    self.assertEqual(n, 1)
    self.assertIs(type(n), int)
    bad_int = BadInt2()
    with self.assertWarns(DeprecationWarning):
        n = int(bad_int)
    self.assertEqual(n, 1)
    self.assertIs(type(n), int)
    bad_int = TruncReturnsBadIndex()
    with self.assertWarns(DeprecationWarning):
        n = int(bad_int)
    self.assertEqual(n, 1)
    self.assertIs(type(n), int)
    bad_int = TruncReturnsBadInt()
    self.assertRaises(TypeError, int, bad_int)
    good_int = TruncReturnsIntSubclass()
    n = int(good_int)
    self.assertEqual(n, 1)
    self.assertIs(type(n), int)
    n = IntSubclass(good_int)
    self.assertEqual(n, 1)
    self.assertIs(type(n), IntSubclass)
