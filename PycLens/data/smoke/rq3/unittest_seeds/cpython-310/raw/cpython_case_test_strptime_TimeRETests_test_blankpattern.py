# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: TimeRETests_test_blankpattern

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_locale = _strptime.LocaleTime()
    test_locale.timezone = (frozenset(), frozenset())
    self.assertEqual(_strptime.TimeRE(test_locale).pattern('%Z'), '', "with timezone == ('',''), TimeRE().pattern('%Z') != ''")
