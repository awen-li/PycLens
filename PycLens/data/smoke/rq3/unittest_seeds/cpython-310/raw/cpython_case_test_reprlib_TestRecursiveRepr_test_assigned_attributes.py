# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: TestRecursiveRepr_test_assigned_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from functools import WRAPPER_ASSIGNMENTS as assigned
    wrapped = MyContainer3.wrapped
    wrapper = MyContainer3.wrapper
    for name in assigned:
        self.assertIs(getattr(wrapper, name), getattr(wrapped, name))
