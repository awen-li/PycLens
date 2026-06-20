# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: MiscIOTest_test_create_writes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.open(os_helper.TESTFN, 'xb') as f:
        f.write(b'spam')
    with self.open(os_helper.TESTFN, 'rb') as f:
        self.assertEqual(b'spam', f.read())
