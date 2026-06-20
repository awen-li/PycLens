# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: StrptimeTests_test_defaults

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    defaults = (1900, 1, 1, 0, 0, 0, 0, 1, -1)
    strp_output = _strptime._strptime_time('1', '%m')
    self.assertTrue(strp_output == defaults, 'Default values for strptime() are incorrect; %s != %s' % (strp_output, defaults))
