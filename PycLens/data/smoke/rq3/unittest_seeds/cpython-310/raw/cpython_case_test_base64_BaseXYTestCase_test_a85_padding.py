# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_a85_padding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(base64.a85encode(b'x', pad=True), b'GQ7^D')
    eq(base64.a85encode(b'xx', pad=True), b"G^'2g")
    eq(base64.a85encode(b'xxx', pad=True), b'G^+H5')
    eq(base64.a85encode(b'xxxx', pad=True), b'G^+IX')
    eq(base64.a85encode(b'xxxxx', pad=True), b'G^+IXGQ7^D')
    eq(base64.a85decode(b'GQ7^D'), b'x\x00\x00\x00')
    eq(base64.a85decode(b"G^'2g"), b'xx\x00\x00')
    eq(base64.a85decode(b'G^+H5'), b'xxx\x00')
    eq(base64.a85decode(b'G^+IX'), b'xxxx')
    eq(base64.a85decode(b'G^+IXGQ7^D'), b'xxxxx\x00\x00\x00')
