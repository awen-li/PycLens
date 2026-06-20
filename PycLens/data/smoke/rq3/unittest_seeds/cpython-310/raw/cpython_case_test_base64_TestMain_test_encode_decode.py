# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: TestMain_test_encode_decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    output = self.get_output('-t')
    self.assertSequenceEqual(output.splitlines(), (b"b'Aladdin:open sesame'", b"b'QWxhZGRpbjpvcGVuIHNlc2FtZQ==\\n'", b"b'Aladdin:open sesame'"))
