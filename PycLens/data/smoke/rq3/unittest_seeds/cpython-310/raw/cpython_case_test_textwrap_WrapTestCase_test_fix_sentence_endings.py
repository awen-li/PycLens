# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: WrapTestCase_test_fix_sentence_endings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    wrapper = TextWrapper(60, fix_sentence_endings=True)
    text = 'A short line. Note the single space.'
    expect = ['A short line.  Note the single space.']
    self.check(wrapper.wrap(text), expect)
    text = 'Well, Doctor? What do you think?'
    expect = ['Well, Doctor?  What do you think?']
    self.check(wrapper.wrap(text), expect)
    text = 'Well, Doctor?\nWhat do you think?'
    self.check(wrapper.wrap(text), expect)
    text = 'I say, chaps! Anyone for "tennis?"\nHmmph!'
    expect = ['I say, chaps!  Anyone for "tennis?"  Hmmph!']
    self.check(wrapper.wrap(text), expect)
    wrapper.width = 20
    expect = ['I say, chaps!', 'Anyone for "tennis?"', 'Hmmph!']
    self.check(wrapper.wrap(text), expect)
    text = 'And she said, "Go to hell!"\nCan you believe that?'
    expect = ['And she said, "Go to', 'hell!"  Can you', 'believe that?']
    self.check(wrapper.wrap(text), expect)
    wrapper.width = 60
    expect = ['And she said, "Go to hell!"  Can you believe that?']
    self.check(wrapper.wrap(text), expect)
    text = 'File stdio.h is nice.'
    expect = ['File stdio.h is nice.']
    self.check(wrapper.wrap(text), expect)
