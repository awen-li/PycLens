# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hmac.py
# case: TestVectorsTestCase_test_with_digestmod_no_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(TypeError, 'required.*digestmod'):
        key = b'\x0b' * 16
        data = b'Hi There'
        hmac.HMAC(key, data, digestmod=None)
    with self.assertRaisesRegex(TypeError, 'required.*digestmod'):
        hmac.new(key, data)
    with self.assertRaisesRegex(TypeError, 'required.*digestmod'):
        hmac.HMAC(key, msg=data, digestmod='')
