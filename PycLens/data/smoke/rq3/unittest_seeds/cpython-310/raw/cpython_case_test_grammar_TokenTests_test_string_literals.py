# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: TokenTests_test_string_literals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = ''
    y = ''
    self.assertTrue(len(x) == 0 and x == y)
    x = "'"
    y = "'"
    self.assertTrue(len(x) == 1 and x == y and (ord(x) == 39))
    x = '"'
    y = '"'
    self.assertTrue(len(x) == 1 and x == y and (ord(x) == 34))
    x = 'doesn\'t "shrink" does it'
    y = 'doesn\'t "shrink" does it'
    self.assertTrue(len(x) == 24 and x == y)
    x = 'does "shrink" doesn\'t it'
    y = 'does "shrink" doesn\'t it'
    self.assertTrue(len(x) == 24 and x == y)
    x = '\nThe "quick"\nbrown fox\njumps over\nthe \'lazy\' dog.\n'
    y = '\nThe "quick"\nbrown fox\njumps over\nthe \'lazy\' dog.\n'
    self.assertEqual(x, y)
    y = '\nThe "quick"\nbrown fox\njumps over\nthe \'lazy\' dog.\n'
    self.assertEqual(x, y)
    y = '\nThe "quick"\nbrown fox\njumps over\nthe \'lazy\' dog.\n'
    self.assertEqual(x, y)
    y = '\nThe "quick"\nbrown fox\njumps over\nthe \'lazy\' dog.\n'
    self.assertEqual(x, y)
