# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imghdr.py
# case: TestImghdr_test_invalid_headers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for header in (b'\x89PN\r\n', b'\x01\xd9', b'Y\xa6', b'cutecat', b'000000JFI', b'GIF80'):
        self.assertIsNone(imghdr.what(None, header))
