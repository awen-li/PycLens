# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: UnseekableTests_test_open_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for wrapper in (lambda f: f, Tellable, Unseekable):
        with self.subTest(wrapper=wrapper):
            f = io.BytesIO()
            f.write(b'abc')
            bf = io.BufferedWriter(f)
            with zipfile.ZipFile(wrapper(bf), 'w', zipfile.ZIP_STORED) as zipf:
                with zipf.open('ones', 'w') as zopen:
                    zopen.write(b'111')
                with zipf.open('twos', 'w') as zopen:
                    zopen.write(b'222')
            self.assertEqual(f.getvalue()[:5], b'abcPK')
            with zipfile.ZipFile(f) as zipf:
                self.assertEqual(zipf.read('ones'), b'111')
                self.assertEqual(zipf.read('twos'), b'222')
