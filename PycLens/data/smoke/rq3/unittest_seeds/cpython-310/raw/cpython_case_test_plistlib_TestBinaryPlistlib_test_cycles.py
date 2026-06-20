# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestBinaryPlistlib_test_cycles

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = []
    a.append(a)
    b = plistlib.loads(plistlib.dumps(a, fmt=plistlib.FMT_BINARY))
    self.assertIs(b[0], b)
    a = ([],)
    a[0].append(a)
    b = plistlib.loads(plistlib.dumps(a, fmt=plistlib.FMT_BINARY))
    self.assertIs(b[0][0], b)
    a = {}
    a['x'] = a
    b = plistlib.loads(plistlib.dumps(a, fmt=plistlib.FMT_BINARY))
    self.assertIs(b['x'], b)
