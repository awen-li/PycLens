# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_bad_open_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN, mode='w') as zipf:
        zipf.writestr('foo.txt', 'O, for a Muse of Fire!')
    with zipfile.ZipFile(TESTFN, mode='r') as zipf:
        zipf.read('foo.txt')
        self.assertRaises(ValueError, zipf.open, 'foo.txt', 'q')
        self.assertRaises(ValueError, zipf.open, 'foo.txt', 'U')
        self.assertRaises(ValueError, zipf.open, 'foo.txt', 'rU')
