# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: WrapTestCase_test_simple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = "Hello there, how are you this fine day?  I'm glad to hear it!"
    self.check_wrap(text, 12, ['Hello there,', 'how are you', 'this fine', "day?  I'm", 'glad to hear', 'it!'])
    self.check_wrap(text, 42, ['Hello there, how are you this fine day?', "I'm glad to hear it!"])
    self.check_wrap(text, 80, [text])
