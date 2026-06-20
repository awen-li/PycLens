# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestOptionChecks_test_callback_not_callable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertOptionError("option -b: callback not callable: 'foo'", ['-b'], {'action': 'callback', 'callback': 'foo'})
