# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionDocstringTest_test_set_docstring_attr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.b.__doc__, None)
    docstr = 'A test method that does nothing'
    self.b.__doc__ = docstr
    self.F.a.__doc__ = docstr
    self.assertEqual(self.b.__doc__, docstr)
    self.assertEqual(self.fi.a.__doc__, docstr)
    self.cannot_set_attr(self.fi.a, '__doc__', docstr, AttributeError)
