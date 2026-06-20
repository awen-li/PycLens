# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hmac.py
# case: TestVectorsTestCase_test_sha384_rfc4231

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._rfc4231_test_cases(hashlib.sha384, 'sha384', 48, 128)
