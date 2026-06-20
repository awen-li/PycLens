# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: NumberTest_test_subclassing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    typecode = self.typecode

    class ExaggeratingArray(array.array):
        __slots__ = ['offset']

        def __new__(cls, typecode, data, offset):
            return array.array.__new__(cls, typecode, data)

        def __init__(self, typecode, data, offset):
            self.offset = offset

        def __getitem__(self, i):
            return array.array.__getitem__(self, i) + self.offset
    a = ExaggeratingArray(self.typecode, [3, 6, 7, 11], 4)
    self.assertEntryEqual(a[0], 7)
    self.assertRaises(AttributeError, setattr, a, 'color', 'blue')
