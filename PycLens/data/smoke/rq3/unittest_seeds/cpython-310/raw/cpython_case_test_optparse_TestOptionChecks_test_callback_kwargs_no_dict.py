# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestOptionChecks_test_callback_kwargs_no_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertOptionError("option -b: callback_kwargs, if supplied, must be a dict: not 'foo'", ['-b'], {'action': 'callback', 'callback': self.dummy, 'callback_kwargs': 'foo'})
