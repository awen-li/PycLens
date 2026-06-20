# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: UstarReadTest_test_fileobj_text

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.tar.extractfile('ustar/regtype') as fobj:
        fobj = io.TextIOWrapper(fobj)
        data = fobj.read().encode('iso8859-1')
        self.assertEqual(sha256sum(data), sha256_regtype)
        try:
            fobj.seek(100)
        except AttributeError:
            self.fail('seeking failed in text mode')
