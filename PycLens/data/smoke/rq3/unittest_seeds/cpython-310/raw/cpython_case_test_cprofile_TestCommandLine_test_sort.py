# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cprofile.py
# case: TestCommandLine_test_sort

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = assert_python_failure('-m', 'cProfile', '-s', 'demo')
    self.assertGreater(rc, 0)
    self.assertIn(b"option -s: invalid choice: 'demo'", err)
