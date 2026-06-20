# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestBinaryPlistlib_test_unsupported

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    unsupported = [*range(1, 8), *range(10, 15), 32, 33, *range(36, 51), *range(52, 64)]
    for i in [112, 144, 176, 192, 224, 240]:
        unsupported.extend((i + j for j in range(16)))
    for token in unsupported:
        with self.subTest(f'token {token:02x}'):
            with self.assertRaises(plistlib.InvalidFileException):
                self.decode(bytes([token]) + b'\x00' * 16)
