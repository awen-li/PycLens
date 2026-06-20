# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestPlistlib_test_controlcharacters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(128):
        c = chr(i)
        testString = 'string containing %s' % c
        if i >= 32 or c in '\r\n\t':
            data = plistlib.dumps(testString, fmt=plistlib.FMT_XML)
            if c != '\r':
                self.assertEqual(plistlib.loads(data), testString)
        else:
            with self.assertRaises(ValueError):
                plistlib.dumps(testString, fmt=plistlib.FMT_XML)
        plistlib.dumps(testString, fmt=plistlib.FMT_BINARY)
