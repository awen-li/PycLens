# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: UstarReadTest_test_fileobj_iter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.tar.extract('ustar/regtype', TEMPDIR, filter='data')
    tarinfo = self.tar.getmember('ustar/regtype')
    with open(os.path.join(TEMPDIR, 'ustar/regtype'), 'r') as fobj1:
        lines1 = fobj1.readlines()
    with self.tar.extractfile(tarinfo) as fobj2:
        lines2 = list(io.TextIOWrapper(fobj2))
        self.assertEqual(lines1, lines2, 'fileobj.__iter__() failed')
