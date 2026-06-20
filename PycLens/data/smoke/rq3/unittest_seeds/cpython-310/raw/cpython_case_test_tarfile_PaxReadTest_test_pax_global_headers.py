# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: PaxReadTest_test_pax_global_headers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tar = tarfile.open(tarname, encoding='iso8859-1')
    try:
        tarinfo = tar.getmember('pax/regtype1')
        self.assertEqual(tarinfo.uname, 'foo')
        self.assertEqual(tarinfo.gname, 'bar')
        self.assertEqual(tarinfo.pax_headers.get('VENDOR.umlauts'), 'ÄÖÜäöüß')
        tarinfo = tar.getmember('pax/regtype2')
        self.assertEqual(tarinfo.uname, '')
        self.assertEqual(tarinfo.gname, 'bar')
        self.assertEqual(tarinfo.pax_headers.get('VENDOR.umlauts'), 'ÄÖÜäöüß')
        tarinfo = tar.getmember('pax/regtype3')
        self.assertEqual(tarinfo.uname, 'tarfile')
        self.assertEqual(tarinfo.gname, 'tarfile')
        self.assertEqual(tarinfo.pax_headers.get('VENDOR.umlauts'), 'ÄÖÜäöüß')
    finally:
        tar.close()
