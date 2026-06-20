# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FSEncodingTests_test_nop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(os.fsencode(b'abc\xff'), b'abc\xff')
    self.assertEqual(os.fsdecode('abcŁ'), 'abcŁ')
