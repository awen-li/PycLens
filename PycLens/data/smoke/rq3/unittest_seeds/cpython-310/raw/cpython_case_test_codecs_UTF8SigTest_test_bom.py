# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF8SigTest_test_bom

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = codecs.getincrementaldecoder('utf-8-sig')()
    s = 'spam'
    self.assertEqual(d.decode(s.encode('utf-8-sig')), s)
