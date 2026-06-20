# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: WrapTestCase_test_non_breaking_space

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = 'This is a sentence with non-breaking\xa0space.'
    self.check_wrap(text, 20, ['This is a sentence', 'with non-', 'breaking\xa0space.'], break_on_hyphens=True)
    self.check_wrap(text, 20, ['This is a sentence', 'with', 'non-breaking\xa0space.'], break_on_hyphens=False)
