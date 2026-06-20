# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: Test_hook_compressed_test_gz_ext_fake

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    original_open = gzip.open
    gzip.open = self.fake_open
    try:
        result = fileinput.hook_compressed('test.gz', 'r')
    finally:
        gzip.open = original_open
    self.assertEqual(self.fake_open.invocation_count, 1)
    self.assertEqual(self.fake_open.last_invocation, (('test.gz', 'r'), {}))
