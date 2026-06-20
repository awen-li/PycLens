# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_misc_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.checkPatternError('(', 'missing ), unterminated subpattern', 0)
    self.checkPatternError('((a|b)', 'missing ), unterminated subpattern', 0)
    self.checkPatternError('(a|b))', 'unbalanced parenthesis', 5)
    self.checkPatternError('(?P', 'unexpected end of pattern', 3)
    self.checkPatternError('(?z)', 'unknown extension ?z', 1)
    self.checkPatternError('(?iz)', 'unknown flag', 3)
    self.checkPatternError('(?i', 'missing -, : or )', 3)
    self.checkPatternError('(?#abc', 'missing ), unterminated comment', 0)
    self.checkPatternError('(?<', 'unexpected end of pattern', 3)
    self.checkPatternError('(?<>)', 'unknown extension ?<>', 1)
    self.checkPatternError('(?', 'unexpected end of pattern', 2)
