# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib_response.py
# case: TestResponse_test_addinfo

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    info = urllib.response.addinfo(self.fp, self.test_headers)
    self.assertEqual(info.info(), self.test_headers)
    self.assertEqual(info.headers, self.test_headers)
