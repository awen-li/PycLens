# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_read0

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN, mode='w') as zipf:
        zipf.writestr('foo.txt', 'O, for a Muse of Fire!')
        with zipf.open('foo.txt') as f:
            for i in range(FIXEDTEST_SIZE):
                self.assertEqual(f.read(0), b'')
            self.assertEqual(f.read(), b'O, for a Muse of Fire!')
