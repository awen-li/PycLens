# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_negative_central_directory_offset_raises_BadZipFile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buffer = bytearray(b'PK\x05\x06' + b'\x00' * 18)
    for dirsize in (1, 2 ** 32 - 1):
        buffer[12:16] = struct.pack('<L', dirsize)
        f = io.BytesIO(buffer)
        self.assertRaises(zipfile.BadZipFile, zipfile.ZipFile, f)
