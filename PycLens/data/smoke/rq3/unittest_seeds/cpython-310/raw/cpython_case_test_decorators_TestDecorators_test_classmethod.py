# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decorators.py
# case: TestDecorators_test_classmethod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    wrapper = self.check_wrapper_attrs(classmethod, '<classmethod({!r})>')
    self.assertRaises(TypeError, wrapper, 1)
