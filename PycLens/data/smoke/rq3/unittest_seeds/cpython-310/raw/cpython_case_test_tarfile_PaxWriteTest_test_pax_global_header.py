# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: PaxWriteTest_test_pax_global_header

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pax_headers = {'foo': 'bar', 'uid': '0', 'mtime': '1.23', 'test': 'äöü', 'äöü': 'test'}
    tar = tarfile.open(tmpname, 'w', format=tarfile.PAX_FORMAT, pax_headers=pax_headers)
    try:
        tar.addfile(tarfile.TarInfo('test'))
    finally:
        tar.close()
    tar = tarfile.open(tmpname, encoding='iso8859-1')
    try:
        self.assertEqual(tar.pax_headers, pax_headers)
        self.assertEqual(tar.getmembers()[0].pax_headers, pax_headers)
        for (key, val) in tar.pax_headers.items():
            self.assertIsNot(type(key), bytes)
            self.assertIsNot(type(val), bytes)
            if key in tarfile.PAX_NUMBER_FIELDS:
                try:
                    tarfile.PAX_NUMBER_FIELDS[key](val)
                except (TypeError, ValueError):
                    self.fail('unable to convert pax header field')
    finally:
        tar.close()
