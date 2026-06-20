# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_getnewargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = 'abc'
    args = text.__getnewargs__()
    self.assertIsNot(args[0], text)
    self.assertEqual(args[0], text)
    self.assertEqual(len(args), 1)
