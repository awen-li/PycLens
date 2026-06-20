# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_inline_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    upper_char = 'Ạ'
    lower_char = 'ạ'
    p = re.compile('.' + upper_char, re.I | re.S)
    q = p.match('\n' + lower_char)
    self.assertTrue(q)
    p = re.compile('.' + lower_char, re.I | re.S)
    q = p.match('\n' + upper_char)
    self.assertTrue(q)
    p = re.compile('(?i).' + upper_char, re.S)
    q = p.match('\n' + lower_char)
    self.assertTrue(q)
    p = re.compile('(?i).' + lower_char, re.S)
    q = p.match('\n' + upper_char)
    self.assertTrue(q)
    p = re.compile('(?is).' + upper_char)
    q = p.match('\n' + lower_char)
    self.assertTrue(q)
    p = re.compile('(?is).' + lower_char)
    q = p.match('\n' + upper_char)
    self.assertTrue(q)
    p = re.compile('(?s)(?i).' + upper_char)
    q = p.match('\n' + lower_char)
    self.assertTrue(q)
    p = re.compile('(?s)(?i).' + lower_char)
    q = p.match('\n' + upper_char)
    self.assertTrue(q)
    self.assertTrue(re.match('(?ix) ' + upper_char, lower_char))
    self.assertTrue(re.match('(?ix) ' + lower_char, upper_char))
    self.assertTrue(re.match(' (?i) ' + upper_char, lower_char, re.X))
    self.assertTrue(re.match('(?x) (?i) ' + upper_char, lower_char))
    self.assertTrue(re.match(' (?x) (?i) ' + upper_char, lower_char, re.X))
    p = upper_char + '(?i)'
    with self.assertWarns(DeprecationWarning) as warns:
        self.assertTrue(re.match(p, lower_char))
    self.assertEqual(str(warns.warnings[0].message), 'Flags not at the start of the expression %r but at position 1' % p)
    self.assertEqual(warns.warnings[0].filename, __file__)
    p = upper_char + '(?i)%s' % ('.?' * 100)
    with self.assertWarns(DeprecationWarning) as warns:
        self.assertTrue(re.match(p, lower_char))
    self.assertEqual(str(warns.warnings[0].message), 'Flags not at the start of the expression %r (truncated) but at position 1' % p[:20])
    self.assertEqual(warns.warnings[0].filename, __file__)
    with warnings.catch_warnings():
        warnings.simplefilter('error', BytesWarning)
        p = b'A(?i)'
        with self.assertWarns(DeprecationWarning) as warns:
            self.assertTrue(re.match(p, b'a'))
        self.assertEqual(str(warns.warnings[0].message), 'Flags not at the start of the expression %r but at position 1' % p)
        self.assertEqual(warns.warnings[0].filename, __file__)
    with self.assertWarns(DeprecationWarning):
        self.assertTrue(re.match('(?s).(?i)' + upper_char, '\n' + lower_char))
    with self.assertWarns(DeprecationWarning):
        self.assertTrue(re.match('(?i) ' + upper_char + ' (?x)', lower_char))
    with self.assertWarns(DeprecationWarning):
        self.assertTrue(re.match(' (?x) (?i) ' + upper_char, lower_char))
    with self.assertWarns(DeprecationWarning):
        self.assertTrue(re.match('^(?i)' + upper_char, lower_char))
    with self.assertWarns(DeprecationWarning):
        self.assertTrue(re.match('$|(?i)' + upper_char, lower_char))
    with self.assertWarns(DeprecationWarning) as warns:
        self.assertTrue(re.match('(?:(?i)' + upper_char + ')', lower_char))
    self.assertRegex(str(warns.warnings[0].message), 'Flags not at the start')
    self.assertEqual(warns.warnings[0].filename, __file__)
    with self.assertWarns(DeprecationWarning) as warns:
        self.assertTrue(re.fullmatch('(^)?(?(1)(?i)' + upper_char + ')', lower_char))
    self.assertRegex(str(warns.warnings[0].message), 'Flags not at the start')
    self.assertEqual(warns.warnings[0].filename, __file__)
    with self.assertWarns(DeprecationWarning) as warns:
        self.assertTrue(re.fullmatch('($)?(?(1)|(?i)' + upper_char + ')', lower_char))
    self.assertRegex(str(warns.warnings[0].message), 'Flags not at the start')
    self.assertEqual(warns.warnings[0].filename, __file__)
