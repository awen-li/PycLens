# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_character_set_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.checkPatternError('[', 'unterminated character set', 0)
    self.checkPatternError('[^', 'unterminated character set', 0)
    self.checkPatternError('[a', 'unterminated character set', 0)
    self.checkPatternError('[a-', 'unterminated character set', 0)
    self.checkPatternError('[\\w-b]', 'bad character range \\w-b', 1)
    self.checkPatternError('[a-\\w]', 'bad character range a-\\w', 1)
    self.checkPatternError('[b-a]', 'bad character range b-a', 1)
