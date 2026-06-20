# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_b85_padding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(base64.b85encode(b'x', pad=True), b'cmMzZ')
    eq(base64.b85encode(b'xx', pad=True), b'cz6H+')
    eq(base64.b85encode(b'xxx', pad=True), b'czAdK')
    eq(base64.b85encode(b'xxxx', pad=True), b'czAet')
    eq(base64.b85encode(b'xxxxx', pad=True), b'czAetcmMzZ')
    eq(base64.b85decode(b'cmMzZ'), b'x\x00\x00\x00')
    eq(base64.b85decode(b'cz6H+'), b'xx\x00\x00')
    eq(base64.b85decode(b'czAdK'), b'xxx\x00')
    eq(base64.b85decode(b'czAet'), b'xxxx')
    eq(base64.b85decode(b'czAetcmMzZ'), b'xxxxx\x00\x00\x00')
