# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_rpartition

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(b'mississippi')
    self.assertEqual(b.rpartition(b'ss'), (b'missi', b'ss', b'ippi'))
    self.assertEqual(b.rpartition(b'i'), (b'mississipp', b'i', b''))
    self.assertEqual(b.rpartition(b'w'), (b'', b'', b'mississippi'))
