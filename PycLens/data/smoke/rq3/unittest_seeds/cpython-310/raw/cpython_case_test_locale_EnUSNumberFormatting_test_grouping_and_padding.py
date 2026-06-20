# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: EnUSNumberFormatting_test_grouping_and_padding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_format('%20.f', -42, grouping=1, out='-42'.rjust(20))
    if self.sep:
        self._test_format('%+10.f', -4200, grouping=1, out=('-4%s200' % self.sep).rjust(10))
        self._test_format('%-10.f', -4200, grouping=1, out=('-4%s200' % self.sep).ljust(10))
