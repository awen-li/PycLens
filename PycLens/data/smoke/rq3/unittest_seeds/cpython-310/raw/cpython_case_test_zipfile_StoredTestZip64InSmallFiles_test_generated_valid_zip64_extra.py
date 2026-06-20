# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: StoredTestZip64InSmallFiles_test_generated_valid_zip64_extra

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_file_size = 8
    expected_compress_size = 8
    expected_header_offset = 0
    expected_content = b'test1234'
    params = ({'file_size_64_set': True, 'file_size_extra': True}, {'compress_size_64_set': True, 'compress_size_extra': True}, {'header_offset_64_set': True, 'header_offset_extra': True})
    for r in range(1, len(params) + 1):
        for combo in itertools.combinations(params, r):
            kwargs = {}
            for c in combo:
                kwargs.update(c)
            with zipfile.ZipFile(io.BytesIO(self.make_zip64_file(**kwargs))) as zf:
                zinfo = zf.infolist()[0]
                self.assertEqual(zinfo.file_size, expected_file_size)
                self.assertEqual(zinfo.compress_size, expected_compress_size)
                self.assertEqual(zinfo.header_offset, expected_header_offset)
                self.assertEqual(zf.read(zinfo), expected_content)
