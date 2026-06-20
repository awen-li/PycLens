# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_modified_uid_negative

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    neg_uid = UID(1)
    neg_uid.data = -1
    with self.assertRaises(ValueError):
        plistlib.dumps(neg_uid, fmt=plistlib.FMT_BINARY)
