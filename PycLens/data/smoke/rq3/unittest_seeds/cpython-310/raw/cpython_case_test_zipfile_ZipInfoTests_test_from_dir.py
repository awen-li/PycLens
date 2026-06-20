# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: ZipInfoTests_test_from_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dirpath = os.path.dirname(os.path.abspath(__file__))
    zi = zipfile.ZipInfo.from_file(dirpath, 'stdlib_tests')
    self.assertEqual(zi.filename, 'stdlib_tests/')
    self.assertTrue(zi.is_dir())
    self.assertEqual(zi.compress_type, zipfile.ZIP_STORED)
    self.assertEqual(zi.file_size, 0)
