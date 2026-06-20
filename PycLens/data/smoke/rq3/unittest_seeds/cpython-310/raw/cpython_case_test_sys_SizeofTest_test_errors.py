# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SizeofTest_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BadSizeof:

        def __sizeof__(self):
            raise ValueError
    self.assertRaises(ValueError, sys.getsizeof, BadSizeof())

    class InvalidSizeof:

        def __sizeof__(self):
            return None
    self.assertRaises(TypeError, sys.getsizeof, InvalidSizeof())
    sentinel = ['sentinel']
    self.assertIs(sys.getsizeof(InvalidSizeof(), sentinel), sentinel)

    class FloatSizeof:

        def __sizeof__(self):
            return 4.5
    self.assertRaises(TypeError, sys.getsizeof, FloatSizeof())
    self.assertIs(sys.getsizeof(FloatSizeof(), sentinel), sentinel)

    class OverflowSizeof(int):

        def __sizeof__(self):
            return int(self)
    self.assertEqual(sys.getsizeof(OverflowSizeof(sys.maxsize)), sys.maxsize + self.gc_headsize)
    with self.assertRaises(OverflowError):
        sys.getsizeof(OverflowSizeof(sys.maxsize + 1))
    with self.assertRaises(ValueError):
        sys.getsizeof(OverflowSizeof(-1))
    with self.assertRaises((ValueError, OverflowError)):
        sys.getsizeof(OverflowSizeof(-sys.maxsize - 1))
