# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF32Test_test_handlers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(('�', 1), codecs.utf_32_decode(b'\x01', 'replace', True))
    self.assertEqual(('', 1), codecs.utf_32_decode(b'\x01', 'ignore', True))
