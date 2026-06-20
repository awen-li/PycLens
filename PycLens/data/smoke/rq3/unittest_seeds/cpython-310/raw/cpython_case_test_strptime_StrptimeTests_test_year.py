# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: StrptimeTests_test_year

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for directive in ('y', 'Y'):
        self.helper(directive, 0)
    for (century, bounds) in ((1900, ('69', '99')), (2000, ('00', '68'))):
        for bound in bounds:
            strp_output = _strptime._strptime_time(bound, '%y')
            expected_result = century + int(bound)
            self.assertTrue(strp_output[0] == expected_result, "'y' test failed; passed in '%s' and returned '%s'" % (bound, strp_output[0]))
