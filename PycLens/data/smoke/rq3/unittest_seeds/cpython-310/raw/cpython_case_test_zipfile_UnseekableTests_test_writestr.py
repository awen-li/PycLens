# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: UnseekableTests_test_writestr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for wrapper in (lambda f: f, Tellable, Unseekable):
        with self.subTest(wrapper=wrapper):
            f = io.BytesIO()
            f.write(b'abc')
            bf = io.BufferedWriter(f)
            with zipfile.ZipFile(wrapper(bf), 'w', zipfile.ZIP_STORED) as zipfp:
                zipfp.writestr('ones', b'111')
                zipfp.writestr('twos', b'222')
            self.assertEqual(f.getvalue()[:5], b'abcPK')
            with zipfile.ZipFile(f, mode='r') as zipf:
                with zipf.open('ones') as zopen:
                    self.assertEqual(zopen.read(), b'111')
                with zipf.open('twos') as zopen:
                    self.assertEqual(zopen.read(), b'222')
