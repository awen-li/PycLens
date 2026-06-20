# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: WrapTestCase_test_hyphenated_numbers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = 'Python 1.0.0 was released on 1994-01-26.  Python 1.0.1 was\nreleased on 1994-02-15.'
    self.check_wrap(text, 30, ['Python 1.0.0 was released on', '1994-01-26.  Python 1.0.1 was', 'released on 1994-02-15.'])
    self.check_wrap(text, 40, ['Python 1.0.0 was released on 1994-01-26.', 'Python 1.0.1 was released on 1994-02-15.'])
    self.check_wrap(text, 1, text.split(), break_long_words=False)
    text = 'I do all my shopping at 7-11.'
    self.check_wrap(text, 25, ['I do all my shopping at', '7-11.'])
    self.check_wrap(text, 27, ['I do all my shopping at', '7-11.'])
    self.check_wrap(text, 29, ['I do all my shopping at 7-11.'])
    self.check_wrap(text, 1, text.split(), break_long_words=False)
