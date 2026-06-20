# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: MaxLinesTestCase_test_spaces

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_wrap(self.text, 12, ['Hello there,', 'how are you', 'this fine', 'day? [...]'], max_lines=4)
    self.check_wrap(self.text, 6, ['Hello', '[...]'], max_lines=2)
    self.check_wrap(self.text + ' ' * 10, 12, ['Hello there,', 'how are you', 'this fine', "day?  I'm", 'glad to hear', 'it!'], max_lines=6)
