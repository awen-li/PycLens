# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_modified_uid_huge

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    huge_uid = UID(1)
    huge_uid.data = 2 ** 64
    with self.assertRaises(OverflowError):
        plistlib.dumps(huge_uid, fmt=plistlib.FMT_BINARY)
