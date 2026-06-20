# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: CAPI_TestCase_test_read_object_from_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    obj = ('€', b'abc', 123, 45.6, 7 + 8j)
    for v in range(marshal.version + 1):
        data = marshal.dumps(obj, v)
        with open(os_helper.TESTFN, 'wb') as f:
            f.write(data + b'xxxx')
        (r, p) = _testcapi.pymarshal_read_object_from_file(os_helper.TESTFN)
        os_helper.unlink(os_helper.TESTFN)
        self.assertEqual(r, obj)
        self.assertEqual(p, len(data))
        with open(os_helper.TESTFN, 'wb') as f:
            f.write(data[:1])
        with self.assertRaises(EOFError):
            _testcapi.pymarshal_read_object_from_file(os_helper.TESTFN)
        os_helper.unlink(os_helper.TESTFN)
