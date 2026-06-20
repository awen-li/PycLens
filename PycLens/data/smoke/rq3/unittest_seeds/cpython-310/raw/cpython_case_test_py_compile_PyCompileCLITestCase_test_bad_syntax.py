# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_py_compile.py
# case: PyCompileCLITestCase_test_bad_syntax

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bad_syntax = os.path.join(os.path.dirname(__file__), 'badsyntax_3131.py')
    (rc, stdout, stderr) = self.pycompilecmd_failure(bad_syntax)
    self.assertEqual(rc, 1)
    self.assertEqual(stdout, b'')
    self.assertIn(b'SyntaxError', stderr)
