# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyexpat.py
# case: SetAttributeTest_test_specified_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(self.parser.specified_attributes, False)
    for x in (0, 1, 2, 0):
        self.parser.specified_attributes = x
        self.assertIs(self.parser.specified_attributes, bool(x))
