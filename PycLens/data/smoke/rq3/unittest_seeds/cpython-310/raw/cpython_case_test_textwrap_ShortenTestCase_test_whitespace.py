# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: ShortenTestCase_test_whitespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = '\n            This is a  paragraph that  already has\n            line breaks and \t tabs too.'
    self.check_shorten(text, 62, 'This is a paragraph that already has line breaks and tabs too.')
    self.check_shorten(text, 61, 'This is a paragraph that already has line breaks and [...]')
    self.check_shorten('hello      world!  ', 12, 'hello world!')
    self.check_shorten('hello      world!  ', 11, 'hello [...]')
    self.check_shorten('hello      world!  ', 10, '[...]')
