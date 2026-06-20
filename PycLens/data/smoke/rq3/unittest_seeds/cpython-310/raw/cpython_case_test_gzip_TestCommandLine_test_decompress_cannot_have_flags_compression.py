# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestCommandLine_test_decompress_cannot_have_flags_compression

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = assert_python_failure('-m', 'gzip', '--fast', '-d')
    self.assertIn(b'error: argument -d/--decompress: not allowed with argument --fast', err)
    self.assertEqual(out, b'')
