# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_zlib_error_does_not_leak

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with unittest.mock.patch('tarfile.TarInfo.fromtarfile') as mock:
        mock.side_effect = zlib.error
        with self.assertRaises(tarfile.ReadError):
            tarfile.open(self.tarname)
