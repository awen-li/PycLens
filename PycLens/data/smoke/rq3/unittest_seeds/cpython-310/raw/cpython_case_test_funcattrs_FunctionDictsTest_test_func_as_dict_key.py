# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionDictsTest_test_func_as_dict_key

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    value = 'Some string'
    d = {}
    d[self.b] = value
    self.assertEqual(d[self.b], value)
