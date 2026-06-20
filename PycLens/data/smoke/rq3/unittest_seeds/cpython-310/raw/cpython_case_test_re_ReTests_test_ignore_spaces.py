# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_ignore_spaces

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for space in ' \t\n\r\x0b\x0c':
        self.assertTrue(re.fullmatch(space + 'a', 'a', re.VERBOSE))
    for space in (b' ', b'\t', b'\n', b'\r', b'\x0b', b'\x0c'):
        self.assertTrue(re.fullmatch(space + b'a', b'a', re.VERBOSE))
    self.assertTrue(re.fullmatch('(?x) a', 'a'))
    self.assertTrue(re.fullmatch(' (?x) a', 'a', re.VERBOSE))
    self.assertTrue(re.fullmatch('(?x) (?x) a', 'a'))
    self.assertTrue(re.fullmatch(' a(?x: b) c', ' ab c'))
    self.assertTrue(re.fullmatch(' a(?-x: b) c', 'a bc', re.VERBOSE))
    self.assertTrue(re.fullmatch('(?x) a(?-x: b) c', 'a bc'))
    self.assertTrue(re.fullmatch('(?x) a| b', 'a'))
    self.assertTrue(re.fullmatch('(?x) a| b', 'b'))
