# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_readline.py
# case: TestReadline_test_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, stdout, stderr) = assert_python_ok('-c', 'import readline', TERM='xterm-256color')
    self.assertEqual(stdout, b'')
