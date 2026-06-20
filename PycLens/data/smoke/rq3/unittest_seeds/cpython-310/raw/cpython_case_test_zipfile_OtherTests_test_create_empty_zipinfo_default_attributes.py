# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_create_empty_zipinfo_default_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zi = zipfile.ZipInfo()
    self.assertEqual(zi.orig_filename, 'NoName')
    self.assertEqual(zi.filename, 'NoName')
    self.assertEqual(zi.date_time, (1980, 1, 1, 0, 0, 0))
    self.assertEqual(zi.compress_type, zipfile.ZIP_STORED)
    self.assertEqual(zi.comment, b'')
    self.assertEqual(zi.extra, b'')
    self.assertIn(zi.create_system, (0, 3))
    self.assertEqual(zi.create_version, zipfile.DEFAULT_VERSION)
    self.assertEqual(zi.extract_version, zipfile.DEFAULT_VERSION)
    self.assertEqual(zi.reserved, 0)
    self.assertEqual(zi.flag_bits, 0)
    self.assertEqual(zi.volume, 0)
    self.assertEqual(zi.internal_attr, 0)
    self.assertEqual(zi.external_attr, 0)
    self.assertEqual(zi.file_size, 0)
    self.assertEqual(zi.compress_size, 0)
