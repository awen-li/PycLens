# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_re_groupref_exists_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.checkPatternError('(?P<a>)(?(0)a|b)', 'bad group number', 10)
    self.checkPatternError('()(?(-1)a|b)', "bad character in group name '-1'", 5)
    self.checkPatternError('()(?(㊀)a|b)', "bad character in group name '㊀'", 5)
    self.checkPatternError('()(?(¹)a|b)', "bad character in group name '¹'", 5)
    self.checkPatternError('()(?(1', 'missing ), unterminated name', 5)
    self.checkPatternError('()(?(1)a', 'missing ), unterminated subpattern', 2)
    self.checkPatternError('()(?(1)a|b', 'missing ), unterminated subpattern', 2)
    self.checkPatternError('()(?(1)a|b|c', 'conditional backref with more than two branches', 10)
    self.checkPatternError('()(?(1)a|b|c)', 'conditional backref with more than two branches', 10)
    self.checkPatternError('()(?(2)a)', 'invalid group reference 2', 5)
