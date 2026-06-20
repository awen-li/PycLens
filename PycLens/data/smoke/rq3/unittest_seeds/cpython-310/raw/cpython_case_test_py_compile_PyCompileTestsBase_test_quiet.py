# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_py_compile.py
# case: PyCompileTestsBase_test_quiet

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bad_coding = os.path.join(os.path.dirname(__file__), 'bad_coding2.py')
    with support.captured_stderr() as stderr:
        self.assertIsNone(py_compile.compile(bad_coding, doraise=False, quiet=2))
        self.assertIsNone(py_compile.compile(bad_coding, doraise=True, quiet=2))
        self.assertEqual(stderr.getvalue(), '')
        with self.assertRaises(py_compile.PyCompileError):
            py_compile.compile(bad_coding, doraise=True, quiet=1)
