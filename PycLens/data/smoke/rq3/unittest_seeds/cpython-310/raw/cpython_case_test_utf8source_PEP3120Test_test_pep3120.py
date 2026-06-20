# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_utf8source.py
# case: PEP3120Test_test_pep3120

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('Питон'.encode('utf-8'), b'\xd0\x9f\xd0\xb8\xd1\x82\xd0\xbe\xd0\xbd')
    self.assertEqual('\\П'.encode('utf-8'), b'\\\xd0\x9f')
