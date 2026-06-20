# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code.py
# case: CodeTest_test_newempty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _testcapi
    co = _testcapi.code_newempty('filename', 'funcname', 15)
    self.assertEqual(co.co_filename, 'filename')
    self.assertEqual(co.co_name, 'funcname')
    self.assertEqual(co.co_firstlineno, 15)
