# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: UnsignedNumberTest_test_bytes_extend

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = bytes(self.example)
    a = array.array(self.typecode, self.example)
    a.extend(s)
    self.assertEqual(a, array.array(self.typecode, self.example + self.example))
    a = array.array(self.typecode, self.example)
    a.extend(bytearray(reversed(s)))
    self.assertEqual(a, array.array(self.typecode, self.example + self.example[::-1]))
