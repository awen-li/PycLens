# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: EnUSNumberFormatting_test_grouping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_format('%f', 1024, grouping=1, out='1%s024.000000' % self.sep)
    self._test_format('%f', 102, grouping=1, out='102.000000')
    self._test_format('%f', -42, grouping=1, out='-42.000000')
    self._test_format('%+f', -42, grouping=1, out='-42.000000')
