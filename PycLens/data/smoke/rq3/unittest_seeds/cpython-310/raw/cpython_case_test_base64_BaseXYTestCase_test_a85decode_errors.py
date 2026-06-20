# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_a85decode_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    illegal = (set(range(32)) | set(range(118, 256))) - set(b' \t\n\r\x0b')
    for c in illegal:
        with self.assertRaises(ValueError, msg=bytes([c])):
            base64.a85decode(b'!!!!' + bytes([c]))
        with self.assertRaises(ValueError, msg=bytes([c])):
            base64.a85decode(b'!!!!' + bytes([c]), adobe=False)
        with self.assertRaises(ValueError, msg=bytes([c])):
            base64.a85decode(b'<~!!!!' + bytes([c]) + b'~>', adobe=True)
    self.assertRaises(ValueError, base64.a85decode, b'malformed', adobe=True)
    self.assertRaises(ValueError, base64.a85decode, b'<~still malformed', adobe=True)
    self.assertRaises(ValueError, base64.a85decode, b'<~~>')
    self.assertRaises(ValueError, base64.a85decode, b'<~~>', adobe=False)
    base64.a85decode(b'<~~>', adobe=True)
    self.assertRaises(ValueError, base64.a85decode, b'abcx', adobe=False)
    self.assertRaises(ValueError, base64.a85decode, b'abcdey', adobe=False)
    self.assertRaises(ValueError, base64.a85decode, b'a b\nc', adobe=False, ignorechars=b'')
    self.assertRaises(ValueError, base64.a85decode, b's', adobe=False)
    self.assertRaises(ValueError, base64.a85decode, b's8', adobe=False)
    self.assertRaises(ValueError, base64.a85decode, b's8W', adobe=False)
    self.assertRaises(ValueError, base64.a85decode, b's8W-', adobe=False)
    self.assertRaises(ValueError, base64.a85decode, b's8W-"', adobe=False)
