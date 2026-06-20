# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestOptionChecks_test_callback_args_no_tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertOptionError("option -b: callback_args, if supplied, must be a tuple: not 'foo'", ['-b'], {'action': 'callback', 'callback': self.dummy, 'callback_args': 'foo'})
