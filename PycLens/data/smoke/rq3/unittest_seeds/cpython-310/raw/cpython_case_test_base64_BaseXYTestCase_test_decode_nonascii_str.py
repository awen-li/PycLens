# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_decode_nonascii_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decode_funcs = (base64.b64decode, base64.standard_b64decode, base64.urlsafe_b64decode, base64.b32decode, base64.b16decode, base64.b85decode, base64.a85decode)
    for f in decode_funcs:
        self.assertRaises(ValueError, f, 'with non-ascii Ë')
