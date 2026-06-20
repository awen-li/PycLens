# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: GenericTest_test_no_argument

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for attr in self.common_attributes + self.attributes:
        with self.assertRaises(TypeError):
            getattr(self.pathmodule, attr)()
            raise self.fail('{}.{}() did not raise a TypeError'.format(self.pathmodule.__name__, attr))
