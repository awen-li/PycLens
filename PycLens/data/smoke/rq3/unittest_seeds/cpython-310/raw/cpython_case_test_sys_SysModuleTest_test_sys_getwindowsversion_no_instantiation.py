# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_sys_getwindowsversion_no_instantiation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test.support.get_attribute(sys, 'getwindowsversion')
    self.assert_raise_on_new_sys_type(sys.getwindowsversion())
