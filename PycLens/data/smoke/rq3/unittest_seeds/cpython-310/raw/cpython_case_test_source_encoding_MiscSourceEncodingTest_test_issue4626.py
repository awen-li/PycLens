# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_source_encoding.py
# case: MiscSourceEncodingTest_test_issue4626

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = compile("# coding=latin-1\nÆ = 'Æ'", 'dummy', 'exec')
    d = {}
    exec(c, d)
    self.assertEqual(d['Æ'], 'Æ')
