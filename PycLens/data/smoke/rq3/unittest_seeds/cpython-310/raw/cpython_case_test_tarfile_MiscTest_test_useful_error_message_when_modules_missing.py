# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscTest_test_useful_error_message_when_modules_missing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fname = os.path.join(os.path.dirname(__file__), 'testtar.tar.xz')
    with self.assertRaises(tarfile.ReadError) as excinfo:
        error = (tarfile.CompressionError('lzma module is not available'),)
        with unittest.mock.patch.object(tarfile.TarFile, 'xzopen', side_effect=error):
            tarfile.open(fname)
    self.assertIn("\n- method xz: CompressionError('lzma module is not available')\n", str(excinfo.exception))
