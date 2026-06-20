# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: WrapTestCase_test_hyphenated

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = "this-is-a-useful-feature-for-reformatting-posts-from-tim-peters'ly"
    self.check_wrap(text, 40, ['this-is-a-useful-feature-for-', "reformatting-posts-from-tim-peters'ly"])
    self.check_wrap(text, 41, ['this-is-a-useful-feature-for-', "reformatting-posts-from-tim-peters'ly"])
    self.check_wrap(text, 42, ['this-is-a-useful-feature-for-reformatting-', "posts-from-tim-peters'ly"])
    expect = "this-|is-|a-|useful-|feature-|for-|reformatting-|posts-|from-|tim-|peters'ly".split('|')
    self.check_wrap(text, 1, expect, break_long_words=False)
    self.check_split(text, expect)
    self.check_split('e-mail', ['e-mail'])
    self.check_split('Jelly-O', ['Jelly-O'])
    self.check_split('half-a-crown', 'half-|a-|crown'.split('|'))
