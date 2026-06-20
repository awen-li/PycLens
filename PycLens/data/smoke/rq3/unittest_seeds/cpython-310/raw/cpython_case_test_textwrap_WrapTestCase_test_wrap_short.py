# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: WrapTestCase_test_wrap_short

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = 'This is a\nshort paragraph.'
    self.check_wrap(text, 20, ['This is a short', 'paragraph.'])
    self.check_wrap(text, 40, ['This is a short paragraph.'])
