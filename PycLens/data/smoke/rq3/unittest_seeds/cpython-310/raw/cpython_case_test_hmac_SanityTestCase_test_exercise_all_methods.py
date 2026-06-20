# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hmac.py
# case: SanityTestCase_test_exercise_all_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        h = hmac.HMAC(b'my secret key', digestmod='sha256')
        h.update(b'compute the hash of this text!')
        h.digest()
        h.hexdigest()
        h.copy()
    except Exception:
        self.fail('Exception raised during normal usage of HMAC class.')
