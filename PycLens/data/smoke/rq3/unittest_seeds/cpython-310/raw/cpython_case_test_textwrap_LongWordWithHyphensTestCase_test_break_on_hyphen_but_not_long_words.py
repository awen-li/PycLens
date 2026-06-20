# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: LongWordWithHyphensTestCase_test_break_on_hyphen_but_not_long_words

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = ['We used enyzme', '2-succinyl-6-hydroxy-2,4-cyclohexadiene-1-carboxylate', 'synthase.']
    self.check_wrap(self.text1, 50, expected, break_long_words=False)
    expected = ['We used', 'enyzme', '2-succinyl-6-hydroxy-2,4-cyclohexadiene-1-carboxylate', 'synthase.']
    self.check_wrap(self.text1, 10, expected, break_long_words=False)
    expected = ['1234567890', '-123456789', '0--this_is', '_a_very_lo', 'ng_option_', 'indeed-', 'good-bye"']
    self.check_wrap(self.text2, 10, expected)
