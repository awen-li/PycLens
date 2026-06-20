# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: SyntaxErrorTests_test_non_utf8

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        with open(TESTFN, 'bw') as testfile:
            testfile.write(b'\x89')
        (rc, out, err) = script_helper.assert_python_failure('-Wd', '-X', 'utf8', TESTFN)
        err = err.decode('utf-8').splitlines()
        self.assertIn("SyntaxError: Non-UTF-8 code starting with '\\x89' in file", err[-1])
    finally:
        unlink(TESTFN)
