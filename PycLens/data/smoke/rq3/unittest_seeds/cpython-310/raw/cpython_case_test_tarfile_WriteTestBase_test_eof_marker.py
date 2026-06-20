# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: WriteTestBase_test_eof_marker

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tarfile.open(tmpname, self.mode) as tar:
        t = tarfile.TarInfo('foo')
        t.size = tarfile.RECORDSIZE - tarfile.BLOCKSIZE
        tar.addfile(t, io.BytesIO(b'a' * t.size))
    with self.open(tmpname, 'rb') as fobj:
        self.assertEqual(len(fobj.read()), tarfile.RECORDSIZE * 2)
