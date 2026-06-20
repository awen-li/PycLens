# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_uid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = UID(1)
    self.assertEqual(plistlib.loads(plistlib.dumps(data, fmt=plistlib.FMT_BINARY)), data)
    dict_data = {'uid0': UID(0), 'uid2': UID(2), 'uid8': UID(2 ** 8), 'uid16': UID(2 ** 16), 'uid32': UID(2 ** 32), 'uid63': UID(2 ** 63)}
    self.assertEqual(plistlib.loads(plistlib.dumps(dict_data, fmt=plistlib.FMT_BINARY)), dict_data)
