# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_partition

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(b'mississippi')
    self.assertEqual(b.partition(b'ss'), (b'mi', b'ss', b'issippi'))
    self.assertEqual(b.partition(b'w'), (b'mississippi', b'', b''))
