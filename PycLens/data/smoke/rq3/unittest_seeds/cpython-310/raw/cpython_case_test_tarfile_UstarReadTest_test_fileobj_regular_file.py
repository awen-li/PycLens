# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: UstarReadTest_test_fileobj_regular_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tarinfo = self.tar.getmember('ustar/regtype')
    with self.tar.extractfile(tarinfo) as fobj:
        data = fobj.read()
        self.assertEqual(len(data), tarinfo.size, 'regular file extraction failed')
        self.assertEqual(sha256sum(data), sha256_regtype, 'regular file extraction failed')
