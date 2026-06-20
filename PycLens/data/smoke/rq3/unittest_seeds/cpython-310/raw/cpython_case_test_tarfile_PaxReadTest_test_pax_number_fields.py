# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: PaxReadTest_test_pax_number_fields

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tar = tarfile.open(tarname, encoding='iso8859-1')
    try:
        tarinfo = tar.getmember('pax/regtype4')
        self.assertEqual(tarinfo.size, 7011)
        self.assertEqual(tarinfo.uid, 123)
        self.assertEqual(tarinfo.gid, 123)
        self.assertEqual(tarinfo.mtime, 1041808783.0)
        self.assertEqual(type(tarinfo.mtime), float)
        self.assertEqual(float(tarinfo.pax_headers['atime']), 1041808783.0)
        self.assertEqual(float(tarinfo.pax_headers['ctime']), 1041808783.0)
    finally:
        tar.close()
