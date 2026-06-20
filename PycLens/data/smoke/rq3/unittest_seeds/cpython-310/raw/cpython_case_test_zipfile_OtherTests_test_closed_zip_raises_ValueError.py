# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_closed_zip_raises_ValueError

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = io.BytesIO()
    with zipfile.ZipFile(data, mode='w') as zipf:
        zipf.writestr('foo.txt', 'O, for a Muse of Fire!')
    self.assertRaises(ValueError, zipf.read, 'foo.txt')
    self.assertRaises(ValueError, zipf.open, 'foo.txt')
    self.assertRaises(ValueError, zipf.testzip)
    self.assertRaises(ValueError, zipf.writestr, 'bogus.txt', 'bogus')
    with open(TESTFN, 'w', encoding='utf-8') as f:
        f.write('zipfile test data')
    self.assertRaises(ValueError, zipf.write, TESTFN)
