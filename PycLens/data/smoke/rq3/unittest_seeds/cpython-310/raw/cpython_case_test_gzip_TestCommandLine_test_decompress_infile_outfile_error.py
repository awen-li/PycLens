# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestCommandLine_test_decompress_infile_outfile_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = assert_python_failure('-m', 'gzip', '-d', 'thisisatest.out')
    self.assertEqual(b"filename doesn't end in .gz: 'thisisatest.out'", err.strip())
    self.assertEqual(rc, 1)
    self.assertEqual(out, b'')
