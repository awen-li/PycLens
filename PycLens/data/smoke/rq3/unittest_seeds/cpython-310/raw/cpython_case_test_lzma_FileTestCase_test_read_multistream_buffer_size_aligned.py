# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_read_multistream_buffer_size_aligned

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    saved_buffer_size = _compression.BUFFER_SIZE
    _compression.BUFFER_SIZE = len(COMPRESSED_XZ)
    try:
        with LZMAFile(BytesIO(COMPRESSED_XZ * 5)) as f:
            self.assertEqual(f.read(), INPUT * 5)
    finally:
        _compression.BUFFER_SIZE = saved_buffer_size
