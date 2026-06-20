# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_source_encoding.py
# case: MiscSourceEncodingTest_test_compilestring

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = compile(b"\n# coding: utf-8\nu = '\xc3\xb3'\n", 'dummy', 'exec')
    d = {}
    exec(c, d)
    self.assertEqual(d['u'], 'ó')
