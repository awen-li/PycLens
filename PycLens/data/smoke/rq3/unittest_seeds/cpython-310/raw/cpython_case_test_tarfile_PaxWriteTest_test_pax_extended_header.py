# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: PaxWriteTest_test_pax_extended_header

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pax_headers = {'path': 'foo', 'uid': '123'}
    tar = tarfile.open(tmpname, 'w', format=tarfile.PAX_FORMAT, encoding='iso8859-1')
    try:
        t = tarfile.TarInfo()
        t.name = 'äöü'
        t.uid = 8 ** 8
        t.pax_headers = pax_headers
        tar.addfile(t)
    finally:
        tar.close()
    tar = tarfile.open(tmpname, encoding='iso8859-1')
    try:
        t = tar.getmembers()[0]
        self.assertEqual(t.pax_headers, pax_headers)
        self.assertEqual(t.name, 'foo')
        self.assertEqual(t.uid, 123)
    finally:
        tar.close()
