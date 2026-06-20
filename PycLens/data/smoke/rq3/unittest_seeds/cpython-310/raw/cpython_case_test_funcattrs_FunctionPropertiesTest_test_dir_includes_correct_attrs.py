# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionPropertiesTest_test_dir_includes_correct_attrs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.b.known_attr = 7
    self.assertIn('known_attr', dir(self.b), 'set attributes not in dir listing of method')
    self.F.a.known_attr = 7
    self.assertIn('known_attr', dir(self.fi.a), 'set attribute on function implementations, should show up in next dir')
