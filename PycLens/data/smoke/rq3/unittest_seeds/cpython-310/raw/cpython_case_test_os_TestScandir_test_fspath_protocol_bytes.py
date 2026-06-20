# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestScandir_test_fspath_protocol_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bytes_filename = os.fsencode('bytesfile.txt')
    bytes_entry = self.create_file_entry(name=bytes_filename)
    fspath = os.fspath(bytes_entry)
    self.assertIsInstance(fspath, bytes)
    self.assertEqual(fspath, os.path.join(os.fsencode(self.path), bytes_filename))
