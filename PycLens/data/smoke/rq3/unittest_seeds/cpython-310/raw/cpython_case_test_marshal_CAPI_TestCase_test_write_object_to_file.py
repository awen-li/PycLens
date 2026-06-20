# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: CAPI_TestCase_test_write_object_to_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    obj = ('€', b'abc', 123, 45.6, 7 + 8j, 'long line ' * 1000)
    for v in range(marshal.version + 1):
        _testcapi.pymarshal_write_object_to_file(obj, os_helper.TESTFN, v)
        with open(os_helper.TESTFN, 'rb') as f:
            data = f.read()
        os_helper.unlink(os_helper.TESTFN)
        self.assertEqual(marshal.loads(data), obj)
