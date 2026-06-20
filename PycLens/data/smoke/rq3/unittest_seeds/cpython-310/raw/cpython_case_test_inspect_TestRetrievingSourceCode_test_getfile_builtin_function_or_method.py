# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestRetrievingSourceCode_test_getfile_builtin_function_or_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError) as e_abs:
        inspect.getfile(abs)
    self.assertIn('expected, got', str(e_abs.exception))
    with self.assertRaises(TypeError) as e_append:
        inspect.getfile(list.append)
    self.assertIn('expected, got', str(e_append.exception))
