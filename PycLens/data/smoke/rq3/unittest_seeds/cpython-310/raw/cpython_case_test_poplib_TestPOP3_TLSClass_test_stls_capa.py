# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_poplib.py
# case: TestPOP3_TLSClass_test_stls_capa

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    capa = self.client.capa()
    self.assertFalse(b'STLS' in capa.keys())
