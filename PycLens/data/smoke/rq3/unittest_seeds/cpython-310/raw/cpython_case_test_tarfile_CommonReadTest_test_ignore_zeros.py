# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CommonReadTest_test_ignore_zeros

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = Random(0).randbytes(512)
    for char in (b'\x00', b'a'):
        with self.open(tmpname, 'w') as fobj:
            fobj.write(char * 1024)
            tarinfo = tarfile.TarInfo('foo')
            tarinfo.size = len(data)
            fobj.write(tarinfo.tobuf())
            fobj.write(data)
        tar = tarfile.open(tmpname, mode='r', ignore_zeros=True)
        try:
            self.assertListEqual(tar.getnames(), ['foo'], 'ignore_zeros=True should have skipped the %r-blocks' % char)
        finally:
            tar.close()
