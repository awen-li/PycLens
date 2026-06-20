# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: LongWordTestCase_test_max_lines_long

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_wrap(self.text, 12, ['Did you say ', '"supercalifr', 'agilisticexp', '[...]'], max_lines=4)
