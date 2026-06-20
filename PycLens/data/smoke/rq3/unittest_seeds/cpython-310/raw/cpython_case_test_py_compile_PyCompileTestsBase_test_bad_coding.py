# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_py_compile.py
# case: PyCompileTestsBase_test_bad_coding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bad_coding = os.path.join(os.path.dirname(__file__), 'bad_coding2.py')
    with support.captured_stderr():
        self.assertIsNone(py_compile.compile(bad_coding, doraise=False))
    self.assertFalse(os.path.exists(importlib.util.cache_from_source(bad_coding)))
