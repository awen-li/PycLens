# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_invalid_operations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exc = self.UnsupportedOperation
    with self.open(os_helper.TESTFN, 'w', encoding='utf-8') as fp:
        self.assertRaises(exc, fp.read)
        self.assertRaises(exc, fp.readline)
    with self.open(os_helper.TESTFN, 'wb') as fp:
        self.assertRaises(exc, fp.read)
        self.assertRaises(exc, fp.readline)
    with self.open(os_helper.TESTFN, 'wb', buffering=0) as fp:
        self.assertRaises(exc, fp.read)
        self.assertRaises(exc, fp.readline)
    with self.open(os_helper.TESTFN, 'rb', buffering=0) as fp:
        self.assertRaises(exc, fp.write, b'blah')
        self.assertRaises(exc, fp.writelines, [b'blah\n'])
    with self.open(os_helper.TESTFN, 'rb') as fp:
        self.assertRaises(exc, fp.write, b'blah')
        self.assertRaises(exc, fp.writelines, [b'blah\n'])
    with self.open(os_helper.TESTFN, 'r', encoding='utf-8') as fp:
        self.assertRaises(exc, fp.write, 'blah')
        self.assertRaises(exc, fp.writelines, ['blah\n'])
        self.assertRaises(exc, fp.seek, 1, self.SEEK_CUR)
        self.assertRaises(exc, fp.seek, -1, self.SEEK_END)
