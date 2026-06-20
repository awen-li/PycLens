# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyexpat.py
# case: SetAttributeTest_test_invalid_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(AttributeError):
        self.parser.returns_unicode = 1
    with self.assertRaises(AttributeError):
        self.parser.returns_unicode
    self.assertRaises(TypeError, setattr, self.parser, range(15), 0)
    self.assertRaises(TypeError, self.parser.__setattr__, range(15), 0)
    self.assertRaises(TypeError, getattr, self.parser, range(15))
