# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_read_write_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls(BASE)
    (p / 'fileA').write_bytes(b'abcdefg')
    self.assertEqual((p / 'fileA').read_bytes(), b'abcdefg')
    self.assertRaises(TypeError, (p / 'fileA').write_bytes, 'somestr')
    self.assertEqual((p / 'fileA').read_bytes(), b'abcdefg')
