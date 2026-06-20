# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_from_buffer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = self.type2test(array.array('B', [1, 2, 3]))
    self.assertEqual(a, b'\x01\x02\x03')
    a = self.type2test(b'\x01\x02\x03')
    self.assertEqual(a, b'\x01\x02\x03')

    class B(bytes):

        def __index__(self):
            raise TypeError
    self.assertEqual(self.type2test(B(b'foobar')), b'foobar')
