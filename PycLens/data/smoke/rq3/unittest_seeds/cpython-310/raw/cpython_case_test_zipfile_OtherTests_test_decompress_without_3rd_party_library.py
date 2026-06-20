# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_decompress_without_3rd_party_library

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = b'PK\x05\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    zip_file = io.BytesIO(data)
    with zipfile.ZipFile(zip_file, 'w', compression=zipfile.ZIP_BZIP2) as zf:
        zf.writestr('a.txt', b'a')
    with mock.patch('zipfile.bz2', None):
        with zipfile.ZipFile(zip_file) as zf:
            self.assertRaises(RuntimeError, zf.extract, 'a.txt')
