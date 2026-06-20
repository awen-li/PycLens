# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: Test_hook_compressed_test_gz_with_encoding_fake

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    original_open = gzip.open
    gzip.open = lambda filename, mode: io.BytesIO(b'Ex-binary string')
    try:
        result = fileinput.hook_compressed('test.gz', 'r', encoding='utf-8')
    finally:
        gzip.open = original_open
    self.assertEqual(list(result), ['Ex-binary string'])
