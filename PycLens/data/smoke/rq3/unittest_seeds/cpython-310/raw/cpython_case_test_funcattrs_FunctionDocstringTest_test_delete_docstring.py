# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionDocstringTest_test_delete_docstring

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.b.__doc__ = 'The docstring'
    del self.b.__doc__
    self.assertEqual(self.b.__doc__, None)
