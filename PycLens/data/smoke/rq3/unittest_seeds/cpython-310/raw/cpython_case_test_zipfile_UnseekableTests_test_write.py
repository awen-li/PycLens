# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: UnseekableTests_test_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for wrapper in (lambda f: f, Tellable, Unseekable):
        with self.subTest(wrapper=wrapper):
            f = io.BytesIO()
            f.write(b'abc')
            bf = io.BufferedWriter(f)
            with zipfile.ZipFile(wrapper(bf), 'w', zipfile.ZIP_STORED) as zipfp:
                self.addCleanup(unlink, TESTFN)
                with open(TESTFN, 'wb') as f2:
                    f2.write(b'111')
                zipfp.write(TESTFN, 'ones')
                with open(TESTFN, 'wb') as f2:
                    f2.write(b'222')
                zipfp.write(TESTFN, 'twos')
            self.assertEqual(f.getvalue()[:5], b'abcPK')
            with zipfile.ZipFile(f, mode='r') as zipf:
                with zipf.open('ones') as zopen:
                    self.assertEqual(zopen.read(), b'111')
                with zipf.open('twos') as zopen:
                    self.assertEqual(zopen.read(), b'222')
