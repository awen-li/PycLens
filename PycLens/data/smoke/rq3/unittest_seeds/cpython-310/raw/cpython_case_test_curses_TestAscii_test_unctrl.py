# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestAscii_test_unctrl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    unctrl = curses.ascii.unctrl
    self.assertEqual(unctrl('a'), 'a')
    self.assertEqual(unctrl('A'), 'A')
    self.assertEqual(unctrl(';'), ';')
    self.assertEqual(unctrl(' '), ' ')
    self.assertEqual(unctrl('\x7f'), '^?')
    self.assertEqual(unctrl('\n'), '^J')
    self.assertEqual(unctrl('\x00'), '^@')
    self.assertEqual(unctrl(ord('A')), 'A')
    self.assertEqual(unctrl(ord('\n')), '^J')
    self.assertEqual(unctrl('\x8a'), '!^J')
    self.assertEqual(unctrl('Á'), '!A')
    self.assertEqual(unctrl(ord('\x8a')), '!^J')
    self.assertEqual(unctrl(ord('Á')), '!A')
