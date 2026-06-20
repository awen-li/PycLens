# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: StoredTestZip64InSmallFiles_test_bad_zip64_extra

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    missing_file_size_extra = self.make_zip64_file(file_size_64_set=True)
    with self.assertRaises(zipfile.BadZipFile) as e:
        zipfile.ZipFile(io.BytesIO(missing_file_size_extra))
    self.assertIn('file size', str(e.exception).lower())
    missing_compress_size_extra = self.make_zip64_file(file_size_64_set=True, file_size_extra=True, compress_size_64_set=True)
    with self.assertRaises(zipfile.BadZipFile) as e:
        zipfile.ZipFile(io.BytesIO(missing_compress_size_extra))
    self.assertIn('compress size', str(e.exception).lower())
    missing_compress_size_extra = self.make_zip64_file(compress_size_64_set=True)
    with self.assertRaises(zipfile.BadZipFile) as e:
        zipfile.ZipFile(io.BytesIO(missing_compress_size_extra))
    self.assertIn('compress size', str(e.exception).lower())
    missing_header_offset_extra = self.make_zip64_file(file_size_64_set=True, file_size_extra=True, compress_size_64_set=True, compress_size_extra=True, header_offset_64_set=True)
    with self.assertRaises(zipfile.BadZipFile) as e:
        zipfile.ZipFile(io.BytesIO(missing_header_offset_extra))
    self.assertIn('header offset', str(e.exception).lower())
    missing_header_offset_extra = self.make_zip64_file(file_size_64_set=False, compress_size_64_set=True, compress_size_extra=True, header_offset_64_set=True)
    with self.assertRaises(zipfile.BadZipFile) as e:
        zipfile.ZipFile(io.BytesIO(missing_header_offset_extra))
    self.assertIn('header offset', str(e.exception).lower())
    missing_header_offset_extra = self.make_zip64_file(file_size_64_set=True, file_size_extra=True, compress_size_64_set=False, header_offset_64_set=True)
    with self.assertRaises(zipfile.BadZipFile) as e:
        zipfile.ZipFile(io.BytesIO(missing_header_offset_extra))
    self.assertIn('header offset', str(e.exception).lower())
    missing_header_offset_extra = self.make_zip64_file(file_size_64_set=False, compress_size_64_set=False, header_offset_64_set=True)
    with self.assertRaises(zipfile.BadZipFile) as e:
        zipfile.ZipFile(io.BytesIO(missing_header_offset_extra))
    self.assertIn('header offset', str(e.exception).lower())
