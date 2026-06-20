# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: ZipInfoTests_test_from_file_fileno

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(__file__, 'rb') as f:
        zi = zipfile.ZipInfo.from_file(f.fileno(), 'test')
        self.assertEqual(posixpath.basename(zi.filename), 'test')
        self.assertFalse(zi.is_dir())
        self.assertEqual(zi.file_size, os.path.getsize(__file__))
