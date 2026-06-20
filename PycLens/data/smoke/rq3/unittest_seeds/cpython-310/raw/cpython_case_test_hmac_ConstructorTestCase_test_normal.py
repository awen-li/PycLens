# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hmac.py
# case: ConstructorTestCase_test_normal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        hmac.HMAC(b'key', digestmod='sha256')
    except Exception:
        self.fail('Standard constructor call raised exception.')
