# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_nondictroot

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for fmt in ALL_FORMATS:
        with self.subTest(fmt=fmt):
            test1 = 'abc'
            test2 = [1, 2, 3, 'abc']
            result1 = plistlib.loads(plistlib.dumps(test1, fmt=fmt))
            result2 = plistlib.loads(plistlib.dumps(test2, fmt=fmt))
            self.assertEqual(test1, result1)
            self.assertEqual(test2, result2)
