# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: EnUSNumberFormatting_test_padding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_format('%20.f', -42, grouping=0, out='-42'.rjust(20))
    self._test_format('%+10.f', -4200, grouping=0, out='-4200'.rjust(10))
    self._test_format('%-10.f', 4200, grouping=0, out='4200'.ljust(10))
