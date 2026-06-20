# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_constructor_with_iterable_argument

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, iter(self.example))
    b = array.array(self.typecode, self.example)
    self.assertEqual(a, b)
    self.assertRaises(TypeError, array.array, self.typecode, 10)

    class A:

        def __iter__(self):
            raise UnicodeError
    self.assertRaises(UnicodeError, array.array, self.typecode, A())

    def B():
        raise UnicodeError
        yield None
    self.assertRaises(UnicodeError, array.array, self.typecode, B())
