# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestBinaryPlistlib_test_invalid_binary

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (name, data) in INVALID_BINARY_PLISTS:
        with self.subTest(name):
            with self.assertRaises(plistlib.InvalidFileException):
                plistlib.loads(b'bplist00' + data, fmt=plistlib.FMT_BINARY)
