# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: EnUSNumberFormatting_test_integer_grouping_and_padding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_format('%10d', 4200, grouping=True, out=('4%s200' % self.sep).rjust(10))
    self._test_format('%-10d', -4200, grouping=True, out=('-4%s200' % self.sep).ljust(10))
