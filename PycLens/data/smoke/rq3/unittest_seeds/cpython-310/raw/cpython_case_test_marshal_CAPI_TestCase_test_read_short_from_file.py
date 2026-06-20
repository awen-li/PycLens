# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: CAPI_TestCase_test_read_short_from_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(os_helper.TESTFN, 'wb') as f:
        f.write(b'4\x12xxxx')
    (r, p) = _testcapi.pymarshal_read_short_from_file(os_helper.TESTFN)
    os_helper.unlink(os_helper.TESTFN)
    self.assertEqual(r, 4660)
    self.assertEqual(p, 2)
    with open(os_helper.TESTFN, 'wb') as f:
        f.write(b'\x12')
    with self.assertRaises(EOFError):
        _testcapi.pymarshal_read_short_from_file(os_helper.TESTFN)
    os_helper.unlink(os_helper.TESTFN)
