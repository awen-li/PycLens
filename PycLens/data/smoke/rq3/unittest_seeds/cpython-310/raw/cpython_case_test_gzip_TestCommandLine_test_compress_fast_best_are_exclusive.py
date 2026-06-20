# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestCommandLine_test_compress_fast_best_are_exclusive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = assert_python_failure('-m', 'gzip', '--fast', '--best')
    self.assertIn(b'error: argument --best: not allowed with argument --fast', err)
    self.assertEqual(out, b'')
