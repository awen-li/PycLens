# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_verbose

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = assert_python_ok('-v')
    self.assertNotIn(b'stack overflow', err)
    (rc, out, err) = assert_python_ok('-vv')
    self.assertNotIn(b'stack overflow', err)
