# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HTTPSTest_test_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = client.HTTPSConnection(HOST, TimeoutTest.PORT, timeout=30)
    self.assertEqual(h.timeout, 30)
