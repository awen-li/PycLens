# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: LongWordTestCase_test_nobreak_long

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.wrapper.break_long_words = 0
    self.wrapper.width = 30
    expect = ['Did you say', '"supercalifragilisticexpialidocious?"', 'How *do* you spell that odd', 'word, anyways?']
    result = self.wrapper.wrap(self.text)
    self.check(result, expect)
    result = wrap(self.text, width=30, break_long_words=0)
    self.check(result, expect)
