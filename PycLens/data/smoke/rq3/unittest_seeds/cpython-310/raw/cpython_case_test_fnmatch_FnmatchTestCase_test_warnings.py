# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fnmatch.py
# case: FnmatchTestCase_test_warnings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings.catch_warnings():
        warnings.simplefilter('error', Warning)
        check = self.check_match
        check('[', '[[]')
        check('&', '[a&&b]')
        check('|', '[a||b]')
        check('~', '[a~~b]')
        check(',', '[a-z+--A-Z]')
        check('.', '[a-z--/A-Z]')
