# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: WrapTestCase_test_whitespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = 'This is a paragraph that already has\nline breaks.  But some of its lines are much longer than the others,\nso it needs to be wrapped.\nSome lines are \ttabbed too.\nWhat a mess!\n'
    expect = ['This is a paragraph that already has line', 'breaks.  But some of its lines are much', 'longer than the others, so it needs to be', 'wrapped.  Some lines are  tabbed too.  What a', 'mess!']
    wrapper = TextWrapper(45, fix_sentence_endings=True)
    result = wrapper.wrap(text)
    self.check(result, expect)
    result = wrapper.fill(text)
    self.check(result, '\n'.join(expect))
    text = '\tTest\tdefault\t\ttabsize.'
    expect = ['        Test    default         tabsize.']
    self.check_wrap(text, 80, expect)
    text = '\tTest\tcustom\t\ttabsize.'
    expect = ['    Test    custom      tabsize.']
    self.check_wrap(text, 80, expect, tabsize=4)
