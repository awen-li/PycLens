# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(re.error) as cm:
        re.compile('(€))')
    err = cm.exception
    self.assertIsInstance(err.pattern, str)
    self.assertEqual(err.pattern, '(€))')
    self.assertEqual(err.pos, 3)
    self.assertEqual(err.lineno, 1)
    self.assertEqual(err.colno, 4)
    self.assertIn(err.msg, str(err))
    self.assertIn(' at position 3', str(err))
    self.assertNotIn(' at position 3', err.msg)
    with self.assertRaises(re.error) as cm:
        re.compile(b'(\xa4))')
    err = cm.exception
    self.assertIsInstance(err.pattern, bytes)
    self.assertEqual(err.pattern, b'(\xa4))')
    self.assertEqual(err.pos, 3)
    with self.assertRaises(re.error) as cm:
        re.compile('\n                (\n                    abc\n                )\n                )\n                (\n                ', re.VERBOSE)
    err = cm.exception
    self.assertEqual(err.pos, 77)
    self.assertEqual(err.lineno, 5)
    self.assertEqual(err.colno, 17)
    self.assertIn(err.msg, str(err))
    self.assertIn(' at position 77', str(err))
    self.assertIn('(line 5, column 17)', str(err))
