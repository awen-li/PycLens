# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_write_unicode_filenames

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN, 'w') as zf:
        zf.writestr('foo.txt', 'Test for unicode filename')
        zf.writestr('ö.txt', 'Test for unicode filename')
        self.assertIsInstance(zf.infolist()[0].filename, str)
    with zipfile.ZipFile(TESTFN, 'r') as zf:
        self.assertEqual(zf.filelist[0].filename, 'foo.txt')
        self.assertEqual(zf.filelist[1].filename, 'ö.txt')
