# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: UstarReadTest_test_fileobj_readlines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.tar.extract('ustar/regtype', TEMPDIR, filter='data')
    tarinfo = self.tar.getmember('ustar/regtype')
    with open(os.path.join(TEMPDIR, 'ustar/regtype'), 'r') as fobj1:
        lines1 = fobj1.readlines()
    with self.tar.extractfile(tarinfo) as fobj:
        fobj2 = io.TextIOWrapper(fobj)
        lines2 = fobj2.readlines()
        self.assertEqual(lines1, lines2, 'fileobj.readlines() failed')
        self.assertEqual(len(lines2), 114, 'fileobj.readlines() failed')
        self.assertEqual(lines2[83], 'I will gladly admit that Python is not the fastest running scripting language.\n', 'fileobj.readlines() failed')
