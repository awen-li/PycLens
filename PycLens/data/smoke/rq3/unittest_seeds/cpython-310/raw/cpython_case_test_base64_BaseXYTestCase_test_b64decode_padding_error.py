# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_b64decode_padding_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(binascii.Error, base64.b64decode, b'abc')
    self.assertRaises(binascii.Error, base64.b64decode, 'abc')
