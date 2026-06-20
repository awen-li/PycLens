# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_b85decode_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    illegal = list(range(33)) + list(b'"\',./:[\\]') + list(range(128, 256))
    for c in illegal:
        with self.assertRaises(ValueError, msg=bytes([c])):
            base64.b85decode(b'0000' + bytes([c]))
    self.assertRaises(ValueError, base64.b85decode, b'|')
    self.assertRaises(ValueError, base64.b85decode, b'|N')
    self.assertRaises(ValueError, base64.b85decode, b'|Ns')
    self.assertRaises(ValueError, base64.b85decode, b'|NsC')
    self.assertRaises(ValueError, base64.b85decode, b'|NsC1')
