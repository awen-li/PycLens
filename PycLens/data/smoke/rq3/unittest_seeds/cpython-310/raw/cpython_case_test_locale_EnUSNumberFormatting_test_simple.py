# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: EnUSNumberFormatting_test_simple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_format('%f', 1024, grouping=0, out='1024.000000')
    self._test_format('%f', 102, grouping=0, out='102.000000')
    self._test_format('%f', -42, grouping=0, out='-42.000000')
    self._test_format('%+f', -42, grouping=0, out='-42.000000')
