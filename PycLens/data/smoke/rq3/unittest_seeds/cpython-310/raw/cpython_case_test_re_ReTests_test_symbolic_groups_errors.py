# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_symbolic_groups_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.checkPatternError('(?P<a>)(?P<a>)', "redefinition of group name 'a' as group 2; was group 1")
    self.checkPatternError('(?P<a>(?P=a))', 'cannot refer to an open group', 10)
    self.checkPatternError('(?Pxy)', 'unknown extension ?Px')
    self.checkPatternError('(?P<a>)(?P=a', 'missing ), unterminated name', 11)
    self.checkPatternError('(?P=', 'missing group name', 4)
    self.checkPatternError('(?P=)', 'missing group name', 4)
    self.checkPatternError('(?P=1)', "bad character in group name '1'", 4)
    self.checkPatternError('(?P=a)', "unknown group name 'a'")
    self.checkPatternError('(?P=a1)', "unknown group name 'a1'")
    self.checkPatternError('(?P=a.)', "bad character in group name 'a.'", 4)
    self.checkPatternError('(?P<)', 'missing >, unterminated name', 4)
    self.checkPatternError('(?P<a', 'missing >, unterminated name', 4)
    self.checkPatternError('(?P<', 'missing group name', 4)
    self.checkPatternError('(?P<>)', 'missing group name', 4)
    self.checkPatternError('(?P<1>)', "bad character in group name '1'", 4)
    self.checkPatternError('(?P<a.>)', "bad character in group name 'a.'", 4)
    self.checkPatternError('(?(', 'missing group name', 3)
    self.checkPatternError('(?())', 'missing group name', 3)
    self.checkPatternError('(?(a))', "unknown group name 'a'", 3)
    self.checkPatternError('(?(-1))', "bad character in group name '-1'", 3)
    self.checkPatternError('(?(1a))', "bad character in group name '1a'", 3)
    self.checkPatternError('(?(a.))', "bad character in group name 'a.'", 3)
    self.checkPatternError('(?P<©>x)', "bad character in group name '©'", 4)
    self.checkPatternError('(?P=©)', "bad character in group name '©'", 4)
    self.checkPatternError('(?(©)y)', "bad character in group name '©'", 3)
