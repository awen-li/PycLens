# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: MaxLinesTestCase_test_placeholder_backtrack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = 'Good grief Python features are advancing quickly!'
    self.check_wrap(text, 12, ['Good grief', 'Python*****'], max_lines=3, placeholder='*****')
