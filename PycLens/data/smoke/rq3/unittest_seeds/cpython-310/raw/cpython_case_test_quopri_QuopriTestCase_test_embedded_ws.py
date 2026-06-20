# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_quopri.py
# case: QuopriTestCase_test_embedded_ws

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (p, e) in self.ESTRINGS:
        self.assertEqual(quopri.encodestring(p, quotetabs=True), e)
        self.assertEqual(quopri.decodestring(e), p)
