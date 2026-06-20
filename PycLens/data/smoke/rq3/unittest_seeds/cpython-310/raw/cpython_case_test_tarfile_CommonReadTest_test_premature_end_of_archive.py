# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CommonReadTest_test_premature_end_of_archive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for size in (512, 600, 1024, 1200):
        with tarfile.open(tmpname, 'w:') as tar:
            t = tarfile.TarInfo('foo')
            t.size = 1024
            tar.addfile(t, io.BytesIO(b'a' * 1024))
        with open(tmpname, 'r+b') as fobj:
            fobj.truncate(size)
        with tarfile.open(tmpname) as tar:
            with self.assertRaisesRegex(tarfile.ReadError, 'unexpected end of data'):
                for t in tar:
                    pass
        with tarfile.open(tmpname) as tar:
            t = tar.next()
            with self.assertRaisesRegex(tarfile.ReadError, 'unexpected end of data'):
                tar.extract(t, TEMPDIR, filter='data')
            with self.assertRaisesRegex(tarfile.ReadError, 'unexpected end of data'):
                tar.extractfile(t).read()
