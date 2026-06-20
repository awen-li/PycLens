# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_print_warning

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_print_warning('msg', 'Warning -- msg\n')
    self.check_print_warning('a\nb', 'Warning -- a\nWarning -- b\n')
