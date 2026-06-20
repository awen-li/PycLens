# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestAscii_test_alt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    alt = curses.ascii.alt
    self.assertEqual(alt('\n'), '\x8a')
    self.assertEqual(alt('A'), 'Á')
    self.assertEqual(alt(ord('A')), 193)
