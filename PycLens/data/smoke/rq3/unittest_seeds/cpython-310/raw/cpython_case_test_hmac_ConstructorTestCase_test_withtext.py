# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hmac.py
# case: ConstructorTestCase_test_withtext

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        h = hmac.HMAC(b'key', b'hash this!', digestmod='sha256')
    except Exception:
        self.fail('Constructor call with text argument raised exception.')
    self.assertEqual(h.hexdigest(), self.expected)
