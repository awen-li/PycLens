# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_scoped_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(re.match('(?i:a)b', 'Ab'))
    self.assertIsNone(re.match('(?i:a)b', 'aB'))
    self.assertIsNone(re.match('(?-i:a)b', 'Ab', re.IGNORECASE))
    self.assertTrue(re.match('(?-i:a)b', 'aB', re.IGNORECASE))
    self.assertIsNone(re.match('(?i:(?-i:a)b)', 'Ab'))
    self.assertTrue(re.match('(?i:(?-i:a)b)', 'aB'))
    self.assertTrue(re.match('\\w(?a:\\W)\\w', 'ààà'))
    self.assertTrue(re.match('(?a:\\W(?u:\\w)\\W)', 'ààà'))
    self.assertTrue(re.match('\\W(?u:\\w)\\W', 'ààà', re.ASCII))
    self.checkPatternError('(?a)(?-a:\\w)', "bad inline flags: cannot turn off flags 'a', 'u' and 'L'", 8)
    self.checkPatternError('(?i-i:a)', 'bad inline flags: flag turned on and off', 5)
    self.checkPatternError('(?au:a)', "bad inline flags: flags 'a', 'u' and 'L' are incompatible", 4)
    self.checkPatternError(b'(?aL:a)', "bad inline flags: flags 'a', 'u' and 'L' are incompatible", 4)
    self.checkPatternError('(?-', 'missing flag', 3)
    self.checkPatternError('(?-+', 'missing flag', 3)
    self.checkPatternError('(?-z', 'unknown flag', 3)
    self.checkPatternError('(?-i', 'missing :', 4)
    self.checkPatternError('(?-i)', 'missing :', 4)
    self.checkPatternError('(?-i+', 'missing :', 4)
    self.checkPatternError('(?-iz', 'unknown flag', 4)
    self.checkPatternError('(?i:', 'missing ), unterminated subpattern', 0)
    self.checkPatternError('(?i', 'missing -, : or )', 3)
    self.checkPatternError('(?i+', 'missing -, : or )', 3)
    self.checkPatternError('(?iz', 'unknown flag', 3)
