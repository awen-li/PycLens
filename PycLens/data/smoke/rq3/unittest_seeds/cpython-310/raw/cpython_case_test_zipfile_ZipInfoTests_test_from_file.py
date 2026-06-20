# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: ZipInfoTests_test_from_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zi = zipfile.ZipInfo.from_file(__file__)
    self.assertEqual(posixpath.basename(zi.filename), 'test_zipfile.py')
    self.assertFalse(zi.is_dir())
    self.assertEqual(zi.file_size, os.path.getsize(__file__))
