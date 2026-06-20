# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_named_unicode_escapes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(re.match('\\N{LESS-THAN SIGN}', '<'))
    self.assertTrue(re.match('\\N{less-than sign}', '<'))
    self.assertIsNone(re.match('\\N{LESS-THAN SIGN}', '>'))
    self.assertTrue(re.match('\\N{SNAKE}', '🐍'))
    self.assertTrue(re.match('\\N{ARABIC LIGATURE UIGHUR KIRGHIZ YEH WITH HAMZA ABOVE WITH ALEF MAKSURA ISOLATED FORM}', 'ﯹ'))
    self.assertTrue(re.match('[\\N{LESS-THAN SIGN}-\\N{GREATER-THAN SIGN}]', '='))
    self.assertIsNone(re.match('[\\N{LESS-THAN SIGN}-\\N{GREATER-THAN SIGN}]', ';'))
    self.checkPatternError('\\N', 'missing {', 2)
    self.checkPatternError('[\\N]', 'missing {', 3)
    self.checkPatternError('\\N{', 'missing character name', 3)
    self.checkPatternError('[\\N{', 'missing character name', 4)
    self.checkPatternError('\\N{}', 'missing character name', 3)
    self.checkPatternError('[\\N{}]', 'missing character name', 4)
    self.checkPatternError('\\NSNAKE}', 'missing {', 2)
    self.checkPatternError('[\\NSNAKE}]', 'missing {', 3)
    self.checkPatternError('\\N{SNAKE', 'missing }, unterminated name', 3)
    self.checkPatternError('[\\N{SNAKE]', 'missing }, unterminated name', 4)
    self.checkPatternError('[\\N{SNAKE]}', "undefined character name 'SNAKE]'", 1)
    self.checkPatternError('\\N{SPAM}', "undefined character name 'SPAM'", 0)
    self.checkPatternError('[\\N{SPAM}]', "undefined character name 'SPAM'", 1)
    self.checkPatternError('\\N{KEYCAP NUMBER SIGN}', "undefined character name 'KEYCAP NUMBER SIGN'", 0)
    self.checkPatternError('[\\N{KEYCAP NUMBER SIGN}]', "undefined character name 'KEYCAP NUMBER SIGN'", 1)
    self.checkPatternError(b'\\N{LESS-THAN SIGN}', 'bad escape \\N', 0)
    self.checkPatternError(b'[\\N{LESS-THAN SIGN}]', 'bad escape \\N', 1)
